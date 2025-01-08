from pydantic import BaseModel, Field
from models.difficulty_level import DifficultyLevel

class VocabularyLessonRequest(BaseModel):
    title: str = Field(min_length=5, max_length=250)
    description: str = Field(min_length=10, max_length=1000)
    difficulty_level: DifficultyLevel
