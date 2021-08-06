#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    connection = engine.connect()
    md = sqlalchemy.MetaData()
    states = sqlalchemy.Table(argv[3], md, autoload=True, autoload_width=engine)
    print(states)
