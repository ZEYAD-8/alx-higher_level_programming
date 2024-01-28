#!/usr/bin/python3
"""
list the first State object from a database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        result = session.query(State).order_by(State.id).first()
        if result:
            print(f"{result.id}: {result.name}")
        else:
            print("Nothing")
