#!/usr/bin/python3

"""
This module prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_city import City, Base
from model_state import Base, State


if __name__ == '__main__':

    usr = argv[1]
    pswd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, pswd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Select columns from 2 classes / tables and print out"""
    cities = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id)

    for city in cities:
        print('{:s}: ({:d}) {:s}'.format(
            city[0], city[1], city[2]))
