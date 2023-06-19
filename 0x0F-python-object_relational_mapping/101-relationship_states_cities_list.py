#!/usr/bin/python3

"""
This module lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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

    states_row = session.query(State).order_by(State.id).all()

    """Use the one-to-many relationship with City to retrieve
    all cities associated to a State
    """
    for state in states_row:
        print("{:d}: {:s}".format(state.id, state.name))
        for city in state.cities:
            print("\t{:d}: {:s}".format(city.id, city.name))

    session.close()
