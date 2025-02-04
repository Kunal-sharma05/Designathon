from fastapi import APIRouter, Depends, status, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import Annotated, List
from core.security import get_current_user
from crud import practice_test as practice_test_service
from schemas.practice_test import PracticeTestRequest
from db.database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/practice-tests", response_model=List[PracticeTestRequest], status_code=status.HTTP_200_OK)
async def read_all_practice_tests(user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    return practice_test_service.get_practice_tests(db)


@router.post("/practice-tests", status_code=status.HTTP_201_CREATED)
async def create_practice_test(practice_test_request: PracticeTestRequest,
                               user: Annotated[dict, Depends(get_current_user)], db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    practice_test_service.add_practice_test(practice_test_request, db)


@router.put("/practice-tests/{test_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_practice_test(practice_test_request: PracticeTestRequest,
                               user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                               test_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    practice_test_service.update_practice_test_by_id(test_id, practice_test_request, db)


@router.delete("/practice-tests", status_code=status.HTTP_204_NO_CONTENT)
async def delete_practice_test(user: Annotated[dict, Depends(get_current_user)], db: db_dependency,
                               test_id: int = Query(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    practice_test_service.delete_practice_test_by_id(test_id, db)
