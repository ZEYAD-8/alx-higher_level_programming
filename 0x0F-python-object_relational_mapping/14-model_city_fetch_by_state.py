#!/usr/bin/python3
"""
prints all City objects from a database
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        result = (
            session.query(State.name, City.id, City.name)
            .join(State, City.state_id == State.id)
            .order_by(City.id)
            .all()
        )

        for row in result:
            print(f"{row[0]}: ({row[1]}) {row[2]}")
