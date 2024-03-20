from models import User, Comment, Session
from create_table import session

# this is first user with two comments
gentle = User(
    username="Gentle",
    email_address="engen.inyang@gmail.com",
    comments=[Comment(text="Software Engineering is fun"),\
              Comment(text="with ALX, mehn is difficult")]
)
# this is the second user with comments also
angel = User(
    username="Blessing",
    email_address="dgentlecute@gmail.com",
    comments=[Comment(text="Make up is my calling"),\
              Comment(text="I love to be loved but i dont love")]
)
# the third user has no comment
peace = User(
    username="Peace",
    email_address="ebrewongpeace@hotmail.com"
)

# to add those valuse, you can use session.add if it was a single user
#if its more than one, then use all, then list the users into a list

session.add_all([gentle, angel, peace])

#then commit the changes to the data base

session.commit()