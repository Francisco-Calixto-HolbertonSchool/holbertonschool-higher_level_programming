#!/usr/bin/python3
'''prints the first State object from the database hbtn_0e_6_usa'''

import sqlalchemy
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
        )
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)
    for st, ci in session.query(State, City).filter(
        State.id == City.state_id
        ).all():
        print('{}: ({}) {}'.format(st.name, ci.id, ci.name))
    session.close()
