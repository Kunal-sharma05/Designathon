from pydantic import BaseModel, Field
from models.difficulty_level import DifficultyLevel

class SpeechLessonRequest(BaseModel):
    title: str = Field(min_length=5, max_length=250)
    audio_content: str = Field(min_length=10, max_length=1000)
    dialogues: str = Field(min_length=10, max_length=5000)
    difficulty_level: DifficultyLevel
