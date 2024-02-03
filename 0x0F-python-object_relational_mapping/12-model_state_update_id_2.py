#!/usr/bin/python3
"""
changes the name of the State object where id=2 to New Mexico from a database
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
        record = session.query(State).filter_by(id=2).first()
        record.name = "New Mexico"
        session.commit()
