from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base

url = "mysql+mysqldb://root:admin8634@localhost/my_db"

Base = declarative_base()

engine = create_engine(url)
connection = engine.connect()
Base.metadata.create_all(engine)

add = text("insert into user (name, nickname) values ('Chidubem', 'Odogwu')")
connection.execute(add)
connection.commit()

query = text("SELECT * FROM user")
get = connection.execute(query)

for x in get:
    print(x)
