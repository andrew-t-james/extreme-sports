from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Categories, Sports, User


from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response
from flask import session as login_session
import httplib2
import json
import requests
import random
import string


engine = create_engine('sqlite:///catalogue.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# api json endpoints
@app.route("/api/users")
def users_api():
    '''Returns a JSON Response for all categories in db'''
    user = session.query(User).all()
    return jsonify(Users=[i.serialize for i in user])


@app.route("/api/categories")
def categories_api():
    '''Returns a JSON Response for all categories in db'''
    category = session.query(Categories).all()
    return jsonify(Categories=[i.serialize for i in category])


@app.route("/api/sports")
def sports_api():
    '''Returns a JSON Response for all sports in db'''
    sports = session.query(Sports).all()
    return jsonify(Sports=[i.serialize for i in sports])


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        print(request.args.get('state'))
        print(login_session['state'])
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.11/me"
    '''
        Due to the formatting for the result from the server token exchange we have to
        split the token first on commas and select the first index which gives us the key : value
        for the server access token then we split it on colons to pull out the actual token value
        and replace the remaining quotes with nothing so that it can be used directly in the graph
        api calls
    '''
    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.11/me?access_token=%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.11/me/picture?access_token=%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (
        facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('index'))
    else:
        flash("You were not logged in")
        return redirect(url_for('index'))


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    print(user)
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# routes for app
@app.route("/")
def index():
    '''Home Route returns a list of all Categories and Renders index page'''
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    categories = session.query(Categories).all()
    return render_template("index.html", categories=categories, STATE=state, logged_in=True)


@app.route("/sport/<int:sport_id>")
def sport_description(sport_id):
    '''Route for individual Sports returns sportdescription page'''
    sport_id = session.query(Sports).filter_by(id=sport_id).first()
    return render_template("sportdescription.html", sport_id=sport_id)


@app.route("/<sport_season>")
def season(sport_season):
    '''Conditionally Render season page based on season'''
    if request.path == '/winter':
        sports = session.query(Sports).join(
            Categories).filter_by(id=1).all()
        return render_template("winter.html", sports=sports, season=sport_season)
    elif request.path == '/summer':
        sports = session.query(Sports).join(
            Categories).filter_by(id=2).all()
        return render_template("summer.html", sports=sports, season=sport_season)
    else:
        return render_template("index.html")


@app.route('/sport/new', methods=['GET', 'POST'])
def new_sport():
    '''Add new Sport Route using GET to render the form,
    POST to submit the new sport to the database'''
    if request.method == 'POST':
        new_sport_to_add = Sports(
            name=request.form['name'],
            description=request.form['description'],
            description_link=request.form['description_link'],
            image_link=request.form['image_link'],
            category_id=request.form['category_id'])

        session.add(new_sport_to_add)
        session.commit()
        # flash("new menu item created!")
        return redirect(url_for('index'))
    else:
        return render_template('newsport.html')


@app.route('/sport/<int:sport_id>/edit', methods=['GET', 'POST'])
def edit_sport(sport_id):
    edited_sport = session.query(Sports).filter_by(id=sport_id).one()

    if request.method == 'POST':
        edited_sport.name = request.form['name']
        edited_sport.description = request.form['description']
        edited_sport.description_link = request.form['description_link']
        edited_sport.image_link = request.form['image_link']
        edited_sport.category_id = request.form['category_id']
        session.commit()
        flash("Item successfully edited")
        return redirect(url_for('sport_description', sport_id=edited_sport.id))
    else:
        return render_template('editsport.html',  sport_id=sport_id, item=edited_sport)


@app.route('/sport/<int:sport_id>/delete', methods=['GET', 'POST'])
def delete_sport(sport_id):
    '''Route search for and to Delete a specific sport from the database'''
    sport_to_delete = session.query(Sports).filter_by(id=sport_id).first()
    if request.method == 'POST':
        session.delete(sport_to_delete)
        session.commit()
        flash("Item deleted")
        return redirect(url_for('index', sport_id=sport_id))
    else:
        return render_template('deleteconfirm.html', sport=sport_to_delete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
