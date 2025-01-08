from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from models.speech_lesson import SpeechLesson
from schemas.speech_lesson import SpeechLessonRequest


db_dependency = Annotated[Session, Depends(get_db)]


def get_speech_lessons(db: db_dependency):
    return db.query(SpeechLesson).all()


def get_speech_lesson_by_id(id: int, db: db_dependency):
    return db.query(SpeechLesson).filter(SpeechLesson.id == id).first()


def delete_speech_lesson_by_id(id: int, db: db_dependency):
    db.query(SpeechLesson).filter(SpeechLesson.id == id).delete()
    db.commit()


def add_speech_lesson(lesson_request: SpeechLessonRequest, db: db_dependency):
    lesson = SpeechLesson(**lesson_request.model_dump())
    db.add(lesson)
    db.commit()


def update_speech_lesson_by_id(id: int, lesson_request: SpeechLessonRequest, db: db_dependency):
    lesson = get_speech_lesson_by_id(id, db)
    if lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    for key, value in lesson_request.model_dump().items():
        setattr(lesson, key, value)
    db.add(lesson)
    db.commit()
