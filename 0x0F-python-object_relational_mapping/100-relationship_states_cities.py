#!/usr/bin/python3
"""Documentation"""
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
