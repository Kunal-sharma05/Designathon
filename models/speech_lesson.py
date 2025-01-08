from db.database import base
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.dialects.mysql import VARCHAR
from models.difficulty_level import DifficultyLevel

class SpeechLesson(base):
    __tablename__ = "speech_lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(250))
    audio_content = Column(VARCHAR(500))  # This could be a URL or file path
    dialogues = Column(VARCHAR(5000))  # Using VARCHAR to store dialogues
    speech_recognition_enabled = Column(VARCHAR(10))  # 'Yes' or 'No'
    difficulty_level = Column(Enum(DifficultyLevel))
