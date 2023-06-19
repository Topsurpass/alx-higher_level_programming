#!/usr/bin/python3

"""
This module lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    usr = argv[1]
    pswd = argv[2]
    db = argv[3]

    """
    Establishes connection to the specified database using
    the provided credentials and configuration.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, pswd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """
    Create new session factory so as to be able to perform
    operations on database
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    """Iterate to retrieve data from state table"""
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
