from fastapi import APIRouter, Depends, status, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import Annotated, List
from core.security import get_current_user

from crud import vocabulary_lesson as vocabulary_lesson_service
from schemas.vocabulary_lesson import VocabularyLessonRequest
from db.database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/vocabulary-lessons", response_model=List[VocabularyLessonRequest], status_code=status.HTTP_200_OK)
async def read_all_vocabulary_lessons(user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    return vocabulary_lesson_service.get_vocabulary_lessons(db)


@router.post("/vocabulary-lessons", status_code=status.HTTP_201_CREATED)
async def create_vocabulary_lesson(vocabulary_lesson_request: VocabularyLessonRequest,
                                   user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    vocabulary_lesson_service.add_vocabulary_lesson(vocabulary_lesson_request, db)


@router.put("/vocabulary-lessons/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_vocabulary_lesson(vocabulary_lesson_request: VocabularyLessonRequest,
                                   user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                                   lesson_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    vocabulary_lesson_service.update_vocabulary_lesson_by_id(lesson_id, vocabulary_lesson_request, db)


@router.delete("/vocabulary-lessons", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vocabulary_lesson(user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                                   lesson_id: int = Query(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    vocabulary_lesson_service.delete_vocabulary_lesson_by_id(lesson_id, db)
