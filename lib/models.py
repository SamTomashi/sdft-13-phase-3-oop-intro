from sqlalchemy import (Column, Integer, String, create_engine, ForeignKey)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Specialty(Base):
    # linking a table to the class
    __tablename__ = "specialties"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    # This helps access all doctors with a specific specialty
    doctors = relationship("Doctor", back_populates="specialty")

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    specialty_id = Column(Integer(), ForeignKey('specialties.id'))

    # This gives access to the speciality related object
    specialty = relationship("Specialty", back_populates="doctors")

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/clinic.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    surgeon = Specialty(name="Surgeon")
    anchologist = Specialty(name="Anchologist")
    cardiologist = Specialty(name="Cardiologist")
    session.bulk_save_objects([surgeon, anchologist, cardiologist])
    session.commit()

    kevin = Doctor(name = "Kevin", specialty=cardiologist)
    mazal = Doctor(name="Mazal", specialty=surgeon)
    brandon = Doctor(name="Brandon", specialty=surgeon)
    session.bulk_save_objects([kevin, mazal])
    session.commit()

    # print(f"{kevin.name} is a {kevin.specialty.name}")

    print([doctor.name for doctor in surgeon.doctors])


    # print(f"the new specialty id is {surgeon.id}")

    # specialties = session.query(Specialty).all()
    # print([specialty.name for specialty in specialties])


    # session.query(Specialty).where(Specialty.id == 2).delete()
    # session.commit()

   



