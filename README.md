# Item Catalog Web App
This web app is a project for the Udacity [FSND Course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About
This project is a RESTful web application utilizing the Flask framework which accesses a SQLLite database that populates extreme sports based on categories. OAuth2 provides authentication, to allow CRUD functionality. Facebook OAuth2 is implemented for accounts.

## In This Repo
This project has one main Python module `app.py` which runs the Flask application. A SQLLite database is created using the `dbsetup.py` module and you can populate the database with test data but is not necessary as db has been populated with data.
The Flask application uses stored HTML templates in the templates folder to build the front-end of the application. CSS/JS/Assets are stored in the static directory.


## Installation
There are some dependencies and a few instructions on how to run the application.
Separate instructions are provided to get GConnect working also.

## Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip file in this directory
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd/vagrant` as instructed in terminal

6. Insert fake data `python dbsetup.py`

```
Only if Data is not present run this command
```

7. Run application using `python app.py`
8. Access the application locally using http://localhost:5000

*Optional step(s)

## JSON Endpoints
The following are open to the public:

Catalog JSON: `/api/categories`
    - Displays the categories.

Sports JSON: `/api/sports`
    - Displays all sports
