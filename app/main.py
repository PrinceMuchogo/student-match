from fastapi import FastAPI
from app.database import engine
import app.models
from app.routes import students

app.models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Roommate Matcher API"
)

app.include_router(students.router, prefix="/api")
