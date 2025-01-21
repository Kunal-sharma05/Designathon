from fastapi import APIRouter, Depends, status, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import Annotated, List
from core.security import get_current_user

from crud import pronunciation_lesson as pronunciation_lesson_service
from schemas.pronunciation_lesson import PronunciationLessonRequest
from db.database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/pronunciation-lessons", response_model=List[PronunciationLessonRequest], status_code=status.HTTP_200_OK)
async def read_all_pronunciation_lessons(user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    return pronunciation_lesson_service.get_pronunciation_lessons(db)


@router.post("/pronunciation-lessons", status_code=status.HTTP_201_CREATED)
async def create_pronunciation_lesson(pronunciation_lesson_request: PronunciationLessonRequest,
                                      user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    pronunciation_lesson_service.add_pronunciation_lesson(pronunciation_lesson_request, db)


@router.put("/pronunciation-lessons/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_pronunciation_lesson(pronunciation_lesson_request: PronunciationLessonRequest,
                                      user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                                      lesson_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    pronunciation_lesson_service.update_pronunciation_lesson_by_id(lesson_id, pronunciation_lesson_request, db)


@router.delete("/pronunciation-lessons", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pronunciation_lesson(user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                                      lesson_id: int = Query(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    pronunciation_lesson_service.delete_pronunciation_lesson_by_id(lesson_id, db)
