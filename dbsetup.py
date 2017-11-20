from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Categories, Sports, User, Base

engine = create_engine('sqlite:///catalogue.db')
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
                       description="Slopestyle is a winter sport"
                       " in which athletes ski or snowboard down a"
                       " course including a variety of obstacles"
                       " including rails, jumps and other terrain"
                       " park features. Points are scored for "
                       "amplitude, originality and quality of tricks."
                       " The discipline has its roots in action sports"
                       " like skateboarding and BMX and has very "
                       "successfully crossed over into the snow sports"
                       " worlds of skiing and snowboard.[1] Twin - tip"
                       " skis are used and are particularly useful if "
                       "the skier lands backwards. Slopestyle tricks fall"
                       " mainly into four categories: spins, grinds, "
                       "grabs and flips. Slopestyle is one of the freestyle"
                       " disciplines, along with moguls, aerials, cross,"
                       " and half - pipe.",
                       description_link='https://en.wikipedia.org"\
                        "/wiki/Slopestyle',
                       image_link="https://coresites-cdn.factorymedia.com/"
                       "mpora_new/wp-content/"
                       "uploads/2014/02/Billy-Jamie-sochi-03.jpg",
                       category=category1)

session.add(winter_sport1)
session.commit()

winter_sport2 = Sports(user_id=1, name="SnowCross",
                       description="Snocross (also snowcross) is a racing"
                       " sport involving racing specialized high performance"
                       " snowmobiles on natural or artificially-made tracks"
                       " consisting of tight turns, banked corners, steep"
                       " jumps and obstacles. Riders race at speed of up to"
                       " 60 miles per hour (96 kilometers per hour).[1] Jumps"
                       " are up to 30 feet (9 meters) tall, so riders travel "
                       "up to 130 feet (40 meters) before they touch the"
                       " ground.[1] According to the World Snowmobile "
                       "Association which governs snocross, watercross,"
                       " and hillcross racing, snocross is the most "
                       "popular form of snowmobile racing.[2]",
                       description_link="https://en.wikipedia.org/"
                       "wiki/Snocross",
                       image_link="https://upload.wikimedia.org/wikipedia"
                       "/commons/thumb/5/58/SnocrossKatejunBobby.jpg/"
                       "500px-SnocrossKatejunBobby.jpg",
                       category=category1)

session.add(winter_sport2)
session.commit()

winter_sport3 = Sports(user_id=1, name="Snowmobile Freestyle",
                       description="The second half of the 20th"
                       " century saw the rise of recreational"
                       " snowmobiling, whose riders are called"
                       " snowmobilers or sledders. Recreational"
                       " riding is known as snowcross/racing, trail"
                       " riding, freestyle, mountain climbing, "
                       "boondocking, carving, ditchbanging and "
                       "grass drags. In the summertime snowmobilers"
                       " can drag race on grass, asphalt strips, or"
                       " even across water (see Snowmobile skipping)."
                       " Snowmobiles are sometimes modified to compete"
                       " in long-distance off-road races such as Trevor"
                       " Erickson's #901 entry in the 2014 Vegas to"
                       " Reno race.", description_link="https://en.wikipedia"
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
                       description="Notable freestyle motocross"
                       " events include Red Bull X-Fighters, "
                       "NIGHT of the JUMPs, the X Games, Gravity"
                       " Games, Big-X, Moto-X Freestyle National"
                       " Championship, and Dew Action Sports Tour."
                       " Freeriding is the original form of "
                       "freestyle motocross which started in "
                       "the hills of southern California; due "
                       "to professional racers such as Jeremy "
                       "McGrath and Phil Lawrence play riding "
                       "in the hills of reche canyon. It has no"
                       " structure, and is traditionally done on"
                       " public land. Riders for natural jumps "
                       "and drop-offs to execute their tricks on."
                       " Some freeriders prefer to jump on sand"
                       " dunes. In many ways, freeriding requires"
                       " more skill and mental ability. Notable"
                       " freeriding locations include Ocotillo"
                       " Wells and Glamis Dunes in California,"
                       " Beaumont, California, and Caineville,"
                       " Utah.",
                       description_link="https://en.wikipedia.org/"
                       "wiki/Freestyle_Motocross",
                       image_link="https://i.ytimg.com/vi/SiULA6_"
                       "td90/maxresdefault.jpg",
                       category=category2)

session.add(summer_sport1)
session.commit()

summer_sport2 = Sports(user_id=1, name="BMX Vert",
                       description="The earliest photographic"
                       " documentation of BMX freestyle shows"
                       " [1] Devin and Todd Bank in 1974 riding"
                       " BMX bikes on an eight foot tall "
                       "skateboard ramp they built at their"
                       " childhood home in West Los Angeles,"
                       " California. This was the birth of BMX"
                       " ramp riding. Devin Bank was also "
                       "documented doing [2] 360 degree freestyle"
                       " spinning tricks on the street and also"
                       " in the air by jumping off curbs. "
                       "Skateboarder Magazine then published"
                       " photos of kids on bikes riding in empty"
                       " household swimming pools in 1975.",
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
                       description="Street skateboarding is"
                       " a style of skateboarding that focuses"
                       " on tricks and transitions in public"
                       " places. Street skateboarders skate in"
                       " urban streets, plazas or industrial"
                       " areas, making use of park benches and"
                       " picnic tables, guard rails and handrails,"
                       " planter boxes, bins, stairs, retaining "
                       "walls and other street furniture not "
                       "purpose-built for skateboarding.",
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
