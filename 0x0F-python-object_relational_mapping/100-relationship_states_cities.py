#!/usr/bin/python3

"""
This module creates the State California with the City San Francisco
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    usr = argv[1]
    pswd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, pswd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Create new state and city"""
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    """Associate the new city to the newly created state"""
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()
