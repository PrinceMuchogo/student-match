from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
import app.schemas, app.crud, app.matcher
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=List[app.schemas.Student])
def create_students_bulk(student_list: app.schemas.StudentList, db: Session = Depends(get_db)):
    return app.crud.create_students_bulk(db, student_list.students)

@router.get("/match", response_model=List[List[app.schemas.Student]])
def match_roommates(db: Session = Depends(get_db)):
    students = app.crud.get_all_students(db)
    matches = app.matcher.match_students(students)
    return [[s1, s2] for s1, s2 in matches]
