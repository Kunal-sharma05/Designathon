from fastapi import APIRouter, Depends, status, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import Annotated, List
from core.security import get_current_user

from crud import speech_lesson as speech_lesson_service
from schemas.speech_lesson import SpeechLessonRequest
from db.database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/speech-lessons", response_model=List[SpeechLessonRequest], status_code=status.HTTP_200_OK)
async def read_all_speech_lessons(user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    return speech_lesson_service.get_speech_lessons(db)


@router.post("/speech-lessons", status_code=status.HTTP_201_CREATED)
async def create_speech_lesson(speech_lesson_request: SpeechLessonRequest,
                               user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    speech_lesson_service.add_speech_lesson(speech_lesson_request, db)


@router.put("/speech-lessons/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_speech_lesson(speech_lesson_request: SpeechLessonRequest,
                               user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                               lesson_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    speech_lesson_service.update_speech_lesson_by_id(lesson_id, speech_lesson_request, db)


@router.delete("/speech-lessons", status_code=status.HTTP_204_NO_CONTENT)
async def delete_speech_lesson(user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                               lesson_id: int = Query(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    speech_lesson_service.delete_speech_lesson_by_id(lesson_id, db)
