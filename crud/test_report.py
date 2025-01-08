from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from models.test_report import TestReport
from schemas.test_report import TestReportRequest



db_dependency = Annotated[Session, Depends(get_db)]


def get_test_reports(db: db_dependency):
    return db.query(TestReport).all()


def get_test_report_by_id(id: int, db: db_dependency):
    return db.query(TestReport).filter(TestReport.id == id).first()


def delete_test_report_by_id(id: int, db: db_dependency):
    db.query(TestReport).filter(TestReport.id == id).delete()
    db.commit()


def add_test_report(report_request: TestReportRequest, db: db_dependency):
    report = TestReport(**report_request.model_dump())
    db.add(report)
    db.commit()


def update_test_report_by_id(id: int, report_request: TestReportRequest, db: db_dependency):
    report = get_test_report_by_id(id, db)
    if report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test Report not found")
    for key, value in report_request.model_dump().items():
        setattr(report, key, value)
    db.add(report)
    db.commit()
