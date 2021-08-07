#!/usr/bin/python3
'''contains the class definition of a State and an instance Base'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Inherit from base'''
    __tablename__ = 'states'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False
        )
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
