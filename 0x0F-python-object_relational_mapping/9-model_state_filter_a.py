#!/usr/bin/python3
"""
list all State objects that contain the letter a from a database
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
        result = session.query(State).filter(State.name.like(f'%a%')).all()
        for record in result:
            print(f"{record.id}: {record.name}")
