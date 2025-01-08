from fastapi import APIRouter, Depends, status, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import Annotated, List

from crud import test_report as test_report_service
from schemas.test_report import TestReportRequest
from db.database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/test-reports", response_model=List[TestReportRequest], status_code=status.HTTP_200_OK)
async def read_all_test_reports(db: db_dependency):
    return test_report_service.get_test_reports(db)


@router.post("/test-reports", status_code=status.HTTP_201_CREATED)
async def create_test_report(test_report_request: TestReportRequest, db: db_dependency):
    test_report_service.add_test_report(test_report_request, db)


@router.put("/test-reports/{report_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_test_report(test_report_request: TestReportRequest, db: db_dependency, report_id: int = Path(gt=0)):
    test_report_service.update_test_report_by_id(report_id, test_report_request, db)


@router.delete("/test-reports", status_code=status.HTTP_204_NO_CONTENT)
async def delete_test_report(db: db_dependency, report_id: int = Query(gt=0)):
    test_report_service.delete_test_report_by_id(report_id, db)
