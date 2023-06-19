#!/usr/bin/python3

"""
This module contains the class definition of a State and an instance
Base = declarative_base()

Each subclass of Base class represent a distinc table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Create new class that inherit from Base class parent.
    The class will be mapped to MySQL table called states
    and each instance of State creates a row in table linked to
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
