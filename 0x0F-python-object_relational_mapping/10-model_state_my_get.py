#!/usr/bin/python3

"""
This module prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    usr = argv[1]
    pswd = argv[2]
    db = argv[3]
    state_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, pswd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        """Filter by searching using name or column"""
        state = session.query(State).filter_by(name=state_name).first()
        if state:
            print(state.id)
        else:
            print('Not found')
    except IndexError as e:
        print(e)

    session.close()
