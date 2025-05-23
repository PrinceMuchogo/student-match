from typing import List
from sqlalchemy.orm import Session
import app.models, app.schemas

def create_students_bulk(db: Session, students: List[app.schemas.StudentCreate]):
    db_students = [app.models.Student(**student.dict()) for student in students]
    db.add_all(db_students)
    db.commit()
    for student in db_students:
        db.refresh(student)
    return db_students

def get_all_students(db: Session):
    return db.query(app.models.Student).all()
