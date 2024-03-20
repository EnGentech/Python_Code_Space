from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
create_engine,
Column,
Integer,
ForeignKey,
String,
)

#creating base class for inheritance
url = 'mysql+mysqldb://root:admin8634@localhost/relationship'
Base = declarative_base()

engine = create_engine(url, echo=True)

"""creating classes """

class parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(40), nullable=False)
    child = relationship("Child", back_populates='parent', uselist = False)
    def __repr__(self):
        return "<Parent {}>".format(self.id)

class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    parent_id = Column(Integer, ForeignKey("parents.id"))
    parent = relationship("Parent", back_populates='child')
    def __repr__(self):
        return "<Child {}>".format(self.id)
