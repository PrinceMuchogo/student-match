from sqlalchemy import Column, Integer, String
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    reg_number = Column(String, unique=True, index=True, nullable=False)
    programme = Column(String, nullable=False)

    gender = Column(String)
    sleeping_schedule = Column(String)
    cleanliness = Column(String)
    noise_tolerance = Column(String)
    smoking = Column(String)
    study_habits = Column(String)
