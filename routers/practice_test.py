from fastapi import APIRouter, Depends, status, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import Annotated, List

from crud import practice_test as practice_test_service
from schemas.practice_test import PracticeTestRequest
from db.database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/practice-tests", response_model=List[PracticeTestRequest], status_code=status.HTTP_200_OK)
async def read_all_practice_tests(db: db_dependency):
    return practice_test_service.get_practice_tests(db)


@router.post("/practice-tests", status_code=status.HTTP_201_CREATED)
async def create_practice_test(practice_test_request: PracticeTestRequest, db: db_dependency):
    practice_test_service.add_practice_test(practice_test_request, db)


@router.put("/practice-tests/{test_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_practice_test(practice_test_request: PracticeTestRequest, db: db_dependency,
                               test_id: int = Path(gt=0)):
    practice_test_service.update_practice_test_by_id(test_id, practice_test_request, db)


@router.delete("/practice-tests", status_code=status.HTTP_204_NO_CONTENT)
async def delete_practice_test(db: db_dependency, test_id: int = Query(gt=0)):
    practice_test_service.delete_practice_test_by_id(test_id, db)
