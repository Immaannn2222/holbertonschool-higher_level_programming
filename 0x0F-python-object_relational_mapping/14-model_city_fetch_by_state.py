#!/usr/bin/python3
"""Documentation"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """my_funct"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city, state in session.query(City, State).filter(
                       City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
