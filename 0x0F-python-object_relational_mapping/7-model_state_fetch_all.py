#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
        )
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
