#!/usr/bin/python3
"""
Module to define the State class and connect it to a MySQL database
using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """State class that links to the MySQL table 'states'"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', 
            pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)
