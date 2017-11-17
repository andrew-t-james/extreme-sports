from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Categories, Sports, Base

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


category1 = Categories(season="Winter")

session.add(category1)
session.commit()

winter_sport1 = Sports(name="Slope Style",
                       description="Slopestyle is a winter sport in which athletes ski or snowboard down a course including a variety of obstacles including rails, jumps and other terrain park features. Points are scored for amplitude, originality and quality of tricks. The discipline has its roots in action sports like skateboarding and BMX and has very successfully crossed over into the snow sports worlds of skiing and snowboard.[1] Twin - tip skis are used and are particularly useful if the skier lands backwards. Slopestyle tricks fall mainly into four categories: spins, grinds, grabs and flips. Slopestyle is one of the freestyle disciplines, along with moguls, aerials, cross, and half - pipe.", description_link='https://en.wikipedia.org/wiki/Slopestyle', image_link="https://coresites-cdn.factorymedia.com/mpora_new/wp-content/uploads/2014/02/Billy-Jamie-sochi-03.jpg", category=category1)

session.add(winter_sport1)
session.commit()

winter_sport2 = Sports(name="SnowCross",
                       description="Snocross (also snowcross) is a racing sport involving racing specialized high performance snowmobiles on natural or artificially-made tracks consisting of tight turns, banked corners, steep jumps and obstacles. Riders race at speed of up to 60 miles per hour (96 kilometers per hour).[1] Jumps are up to 30 feet (9 meters) tall, so riders travel up to 130 feet (40 meters) before they touch the ground.[1] According to the World Snowmobile Association which governs snocross, watercross, and hillcross racing, snocross is the most popular form of snowmobile racing.[2]", description_link="https://en.wikipedia.org/wiki/Snocross", image_link="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/SnocrossKatejunBobby.jpg/500px-SnocrossKatejunBobby.jpg", category=category1)

session.add(winter_sport2)
session.commit()


category2 = Categories(season="Summer")

session.add(category2)
session.commit()


summer_sport1 = Sports(name="Moto X Freestyle",
                       description="Notable freestyle motocross events include Red Bull X-Fighters, NIGHT of the JUMPs, the X Games, Gravity Games, Big-X, Moto-X Freestyle National Championship, and Dew Action Sports Tour. Freeriding is the original form of freestyle motocross which started in the hills of southern California; due to professional racers such as Jeremy McGrath and Phil Lawrence play riding in the hills of reche canyon. It has no structure, and is traditionally done on public land. Riders for natural jumps and drop-offs to execute their tricks on. Some freeriders prefer to jump on sand dunes. In many ways, freeriding requires more skill and mental ability. Notable freeriding locations include Ocotillo Wells and Glamis Dunes in California, Beaumont, California, and Caineville, Utah.", description_link="https://en.wikipedia.org/wiki/Freestyle_Motocross", image_link="https://i.ytimg.com/vi/SiULA6_td90/maxresdefault.jpg", category=category2)

session.add(summer_sport1)
session.commit()

summer_sport2 = Sports(name="BMX Vert",
                       description="Vert is a freestyle BMX discipline performed in a half pipe consisting of two quarter pipes set facing each other (much like a mini ramp), but at around 10–15 feet tall (around 2.5 to 3.5 meters high). The biggest ramp ever used in competition is the X-Games big air ramp at 27 feet (8.2 m) tall. Both ‘faces’ of the ramp have an extension to the transition that is vertical, hence the name. Coping is a round metal tube at the lip of the vert that helps freestyle BMXers do grinds, and stalls on the lip of the vert.", description_link="https://en.wikipedia.org/wiki/Freestyle_BMX#Vert_Ramp", image_link="http://www.promotocross.com/sites/default/files/styles/gallery_small/public/images/gallery/photos/doug-bmx-vert-final-640x370.jpg?itok=nnhd9_fr", category=category2)

session.add(summer_sport2)
session.commit()

# menuItem2 = MenuItem(user_id=1, name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
#                      price="$5.50", course="Entree", restaurant=restaurant1)

# session.add(menuItem2)
# session.commit()


print("added dummy info!")
