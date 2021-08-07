#!/usr/bin/python3
'''prints the first State object from the database hbtn_0e_6_usa'''

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
        )
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)
    martin = State(name='Louisiana')
    session.add(martin)
    print(session.query(State).filter_by(name='Louisiana').all()[0].id)
    session.commit()
    session.close()
