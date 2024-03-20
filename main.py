from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from datetime import datetime

url = "mysql+mysqldb://root:admin8634@localhost/my_db"
Base = declarative_base()
session = sessionmaker()
engine = create_engine(url, echo=True)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(255), nullable=False)
    nickname = Column(String(50))
    date_created = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return ("<User name={}, nickname={}, date_created={}>".format(self.name, self.nickname, self.date_created))
