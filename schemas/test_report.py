from pydantic import BaseModel, Field

class TestReportRequest(BaseModel):
    test_id: int = Field(gt=0)
    user_id: int = Field(gt=0)
    score: float = Field(gt=0, lt=100, description="Score must be between 0 and 100")
    detailed_feedback: str = Field(min_length=5, max_length=1000)
