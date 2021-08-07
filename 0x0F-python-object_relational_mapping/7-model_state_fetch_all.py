#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = sqlalchemy.create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    connection = engine.connect()
    md = sqlalchemy.MetaData(connection).reflect()
    states = md.tables['states']
    print(states)
