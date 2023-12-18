#!/usr/bin/python3
"""Sript that lists all State objects
    from the database hbtn_06_usa
    mysql username, mysql password, database name and state name to search
"""


from model_state import Base, State
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from sys import argv


def list_first_state():
    """Function to check if state exists
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ), pool_pre_ping=True)

    Session = session(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name.like(f'%{argv[4]}%')).all()

    if state:
        for st in state:
            print(f'{st.id}')

    else:
        print('Not found')


if __name__ == '__main__':
    list_first_state()
