#!/usr/bin/python3
"""Sript that lists all State objects
    from the database hbtn_06_usa
    mysql username, mysql password and database name
"""


from model_state import Base, State
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from sys import argv


def change_state_name():
    """Function to change state name
    """
    if __name__ == '__main__':
        change_state_name()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ))

    Session = session(bind=engine)

    Session = Session()

    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()
        session.close()
