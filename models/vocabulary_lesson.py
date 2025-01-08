from db.database import base
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.dialects.mysql import VARCHAR
from models.difficulty_level import DifficultyLevel

class VocabularyLesson(base):
    __tablename__ = "vocabulary_lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(250))
    description = Column(VARCHAR(250))
    difficulty_level = Column(Enum(DifficultyLevel))  # e.g., Beginner, Intermediate, Advanced
    content = Column(VARCHAR(1000))  # Storing AI-generated content in JSON format
    ai_model_version = Column(VARCHAR(250))  # To track the AI model version used for generation
