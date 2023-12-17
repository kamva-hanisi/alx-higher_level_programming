#!/usr/bin/python3
"""Sript that lists all State objects
    from the database hbtn_06_usa
"""


from model_state import Base, State
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ))

    Session = session(bind=engine)

    session = Session()

    state = State(name="Louisiana")

    session.add(state)

    session.commit()

    print(f'{state.id}')
