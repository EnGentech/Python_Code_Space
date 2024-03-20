from models import Base, User, Comment, Session
from connect import engine

session = Session(bind=engine)

"""
At this point we need to use our base class to create our database table
Basically you need to define a metadata object and then add all the class
created into the one single meta object and bind it to one engine for you
to be able to crate you database table.

In this case, the sqlalchemy orm does it in an interesting was by defining
a metadata object as seen below
"""

print("CREATING TABLES >>>")
Base.metadata.create_all(bind=engine)
