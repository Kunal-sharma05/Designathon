from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from models.vocabulary_lesson import VocabularyLesson
from schemas.vocabulary_lesson import VocabularyLessonRequest


db_dependency = Annotated[Session, Depends(get_db)]


def get_vocabulary_lessons(db: db_dependency):
    return db.query(VocabularyLesson).all()


def get_vocabulary_lesson_by_id(id: int, db: db_dependency):
    return db.query(VocabularyLesson).filter(VocabularyLesson.id == id).first()


def delete_vocabulary_lesson_by_id(id: int, db: db_dependency):
    db.query(VocabularyLesson).filter(VocabularyLesson.id == id).delete()
    db.commit()


def add_vocabulary_lesson(lesson_request: VocabularyLessonRequest, db: db_dependency):
    lesson = VocabularyLesson(**lesson_request.model_dump())
    db.add(lesson)
    db.commit()


def update_vocabulary_lesson_by_id(id: int, lesson_request: VocabularyLessonRequest, db: db_dependency):
    lesson = get_vocabulary_lesson_by_id(id, db)
    if lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    for key, value in lesson_request.model_dump().items():
        setattr(lesson, key, value)
    db.add(lesson)
    db.commit()
