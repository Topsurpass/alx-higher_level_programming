#!/usr/bin/python3

"""
This module lists all City objects from the database hbtn_0e_101_usa
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

    city_row = session.query(City).order_by(City.id).all()

    """Use the backref relationship with State to retrieve States
    associated to cities
    """
    for city in city_row:
        print("{:d}: {:s} -> {:s}".format(city.id, city.name, city.state.name))

    session.close()
