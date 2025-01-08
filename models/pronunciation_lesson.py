from db.database import base
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.dialects.mysql import VARCHAR
from models.difficulty_level import DifficultyLevel

class PronunciationLesson(base):
    __tablename__ = "pronunciation_lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(250))
    exercises = Column(VARCHAR(5000))  # Using VARCHAR to store exercises
    feedback = Column(VARCHAR(250))  # Feedback mechanism description
    difficulty_level = Column(Enum(DifficultyLevel))
