from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Categories, Sports, User, Base

engine = create_engine('postgresql://catalog:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


User1 = User(name="Fake User", email="fake@fake.com",
             picture='https://www.communitylandtrust.ca/'
             'wp-content/uploads/2015/10/placeholder.png')
session.add(User1)
session.commit()


category1 = Categories(user_id=1, season="Winter")

session.add(category1)
session.commit()

winter_sport1 = Sports(user_id=1, name="Slope Style",
                       description="Slopestyle is a winter sport in which athletes ski or snowboard down a course including a variety of obstacles.",
                       description_link='https://en.wikipedia.org"\
                        "/wiki/Slopestyle',
                       image_link="https://coresites-cdn.factorymedia.com/"
                       "mpora_new/wp-content/"
                       "uploads/2014/02/Billy-Jamie-sochi-03.jpg",
                       category=category1)

session.add(winter_sport1)
session.commit()

winter_sport2 = Sports(user_id=1, name="SnowCross",
                       description="Snowcross (also snowcross) is a racing sport involving racing specialized high performance snowmobiles.",
                       description_link="https://en.wikipedia.org/"
                       "wiki/Snocross",
                       image_link="https://upload.wikimedia.org/wikipedia"
                       "/commons/thumb/5/58/SnocrossKatejunBobby.jpg/"
                       "500px-SnocrossKatejunBobby.jpg",
                       category=category1)

session.add(winter_sport2)
session.commit()

winter_sport3 = Sports(user_id=1, name="Snowmobile Freestyle",
                       description="The second half of the 20th century saw the rise of recreational snowmobiling, whose riders are called snowmobilers or sledders.",
                       description_link="https://en.wikipedia"
                       ".org/wiki/Snowmobile",
                       image_link="http://kristianbogner.com/wp-content/"
                       "uploads/2012/12/DSC_3660.jpg",
                       category=category1)

session.add(winter_sport3)
session.commit()


category2 = Categories(season="Summer")

session.add(category2)
session.commit()


summer_sport1 = Sports(user_id=1, name="Moto X Freestyle",
                       description="Notable freestyle motocross events include Red Bull X-Fighters.",
                       description_link="https://en.wikipedia.org/"
                       "wiki/Freestyle_Motocross",
                       image_link="https://i.ytimg.com/vi/SiULA6_"
                       "td90/maxresdefault.jpg",
                       category=category2)

session.add(summer_sport1)
session.commit()

summer_sport2 = Sports(user_id=1, name="BMX Vert",
                       description="The earliest photographic documentation of BMX freestyle shows Devin and Todd Bank in 1974 ridingBMX bikes on an eight foot tall skateboard ramp.",
                       description_link="https://en.wikipedia.org/"
                       "wiki/Freestyle_BMX#Vert_Ramp",
                       image_link="http://www.promotocross.com/sites/"
                       "default/files/styles/gallery_small/public/images"
                       "/gallery/photos/doug-bmx-vert-final-640x370."
                       "jpg?itok=nnhd9_fr",
                       category=category2)

session.add(summer_sport2)
session.commit()

summer_sport3 = Sports(user_id=1, name="Skateboard Street",
                       description="Street skateboarding is a style of skateboarding that focuses on tricks and transitions in public places.",
                       description_link="https://en.wikipedia."
                       "org/wiki/Street_skateboarding",
                       image_link="http://a.espncdn.com/media/"
                       "motion/2016/0605/evc_ACTN_20160604_X_Games"
                       "__Austin__FASTCLIPPER__X_99/evc_ACTN_20160604"
                       "_X_Games__Austin__FASTCLIPPER__X_99.jpg",
                       category=category2)

session.add(summer_sport3)
session.commit()


print("added dummy info!")
