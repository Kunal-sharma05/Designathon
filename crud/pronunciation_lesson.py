from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from models.pronunciation_lesson import PronunciationLesson
from schemas.pronunciation_lesson import PronunciationLessonRequest

db_dependency = Annotated[Session, Depends(get_db)]


def get_pronunciation_lessons(db: db_dependency):
    return db.query(PronunciationLesson).all()


def get_pronunciation_lesson_by_id(id: int, db: db_dependency):
    return db.query(PronunciationLesson).filter(PronunciationLesson.id == id).first()


def delete_pronunciation_lesson_by_id(id: int, db: db_dependency):
    db.query(PronunciationLesson).filter(PronunciationLesson.id == id).delete()
    db.commit()


def add_pronunciation_lesson(lesson_request: PronunciationLessonRequest, db: db_dependency):
    lesson = PronunciationLesson(**lesson_request.model_dump())
    db.add(lesson)
    db.commit()


def update_pronunciation_lesson_by_id(id: int, lesson_request: PronunciationLessonRequest, db: db_dependency):
    lesson = get_pronunciation_lesson_by_id(id, db)
    if lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    for key, value in lesson_request.model_dump().items():
        setattr(lesson, key, value)
    db.add(lesson)
    db.commit()
