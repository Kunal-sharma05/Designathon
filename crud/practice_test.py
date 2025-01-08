from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from models.practice_test import PracticeTest
from schemas.practice_test import PracticeTestRequest


db_dependency = Annotated[Session, Depends(get_db)]


def get_practice_tests(db: db_dependency):
    return db.query(PracticeTest).all()


def get_practice_test_by_id(id: int, db: db_dependency):
    return db.query(PracticeTest).filter(PracticeTest.id == id).first()


def delete_practice_test_by_id(id: int, db: db_dependency):
    db.query(PracticeTest).filter(PracticeTest.id == id).delete()
    db.commit()


def add_practice_test(test_request: PracticeTestRequest, db: db_dependency):
    test = PracticeTest(**test_request.model_dump())
    db.add(test)
    db.commit()


def update_practice_test_by_id(id: int, test_request: PracticeTestRequest, db: db_dependency):
    test = get_practice_test_by_id(id, db)
    if test is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Practice Test not found")
    for key, value in test_request.model_dump().items():
        setattr(test, key, value)
    db.add(test)
    db.commit()
