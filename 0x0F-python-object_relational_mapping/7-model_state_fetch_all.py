#!/usr/bin/python3
""" lists all State objects
    from the database hbtn_06_usa
"""


from model_state import Base, State
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from sys import argv


def list_state():
    """Function to list all state objects
    """
    if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ), pool_pre_ping=True)

    Session = session(bind=engine)

    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f'{state.id}: {state.name}')
