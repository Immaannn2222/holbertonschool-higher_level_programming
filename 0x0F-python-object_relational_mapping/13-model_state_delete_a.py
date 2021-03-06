#!/usr/bin/python3
"""Documentation"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """my_funct"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for states in session.query(State).filter(State.name.like('%a%')):
        session.delete(states)
    session.commit()
    session.close()
