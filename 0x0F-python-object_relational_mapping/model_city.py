#!/usr/bin/python3
'''contains the class definition of a State and an instance Base'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    '''Inherit from base'''
    __tablename__ = 'cities'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False
        )
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    state_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('states.id'), nullable=False)
