#!/usr/bin/python3
'''Definition of the City class'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    '''class city'''

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey=('states.id'))
