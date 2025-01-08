from pydantic import BaseModel, Field
from models.difficulty_level import DifficultyLevel

class PronunciationLessonRequest(BaseModel):
    title: str = Field(min_length=5, max_length=250)
    exercises: str = Field(min_length=10, max_length=5000)
    feedback: str = Field(min_length=5, max_length=1000)
    difficulty_level: DifficultyLevel