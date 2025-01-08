from db.database import base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR

class TestReport(base):
    __tablename__ = "test_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user_details.id'))
    test_id = Column(Integer, ForeignKey('practice_tests.id'))
    score = Column(Integer)
    detailed_feedback = Column(VARCHAR(5000))  # Using VARCHAR to store detailed feedback
