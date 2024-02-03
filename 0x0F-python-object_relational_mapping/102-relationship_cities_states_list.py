#!/usr/bin/python3
"""
lists all City objects from a database
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")
