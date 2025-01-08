from db.database import base
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.dialects.mysql import VARCHAR
from models.difficulty_level import DifficultyLevel

class PracticeTest(base):
    __tablename__ = "practice_tests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(250))
    questions = Column(VARCHAR(5000))  # Using VARCHAR to store questions
    results = Column(VARCHAR(1000))  # Using VARCHAR to store results
    difficulty_level = Column(Enum(DifficultyLevel))
