#!/usr/bin/env python3

from sqlalchemy import (Column, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Speciality(Base):
    __tablename__ = 'specialties'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/clinic.db')
    Base.metadata.create_all(engine)

    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()


    # create session, speciality objects

    session.query(Speciality).where(Speciality.id == 1).delete()
    print([(specialty.name) for specialty in session.query(Speciality)])


    # for specialty in session.query(Speciality):
    #     specialty.name = "Pediatrician"

    # session.commit()

    # print([(specialty.name) for specialty in session.query(Speciality)])



