from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base

class City(Base):
    """Class definition of City"""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,\
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

# Coded by EnGentech