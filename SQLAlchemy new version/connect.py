from sqlalchemy import create_engine, text

url = "mysql+mysqldb://root:admin8634@localhost/new_sql"

engine = create_engine(url, echo=True)

"""
creating this connection, we are going to use the with statement,
the with statement basically closes the database after execution 
and possible commit have be completed, rather than using .close, the
the with takes care of that
"""

with engine.connect() as connect:
    """
    with the above, we create our connection using the as connect, hence
    we will be using the connect to communicate with the database, now,
    lets create a means to test our connection by using an sql language.
    This will need us to import the text module which serves as a tool to 
    converting our python string literals into an executeable sql command
    """