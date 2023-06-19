#!/usr/bin/python3

"""
This module prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{:d}: {:s}".format(first_state.id, first_state.name))
    else:
        print('Nothing')

    session.close()
