from pydantic import BaseModel
from typing import List

class StudentBase(BaseModel):
    name: str
    reg_number: str
    programme: str
    gender: str
    sleeping_schedule: str
    cleanliness: str
    noise_tolerance: str
    smoking: str
    study_habits: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class StudentList(BaseModel):
    students: List[StudentCreate]
