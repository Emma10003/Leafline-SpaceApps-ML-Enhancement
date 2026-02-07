from pydantic import BaseModel, Field

class HoneyPredictRequest(BaseModel):
    month: int = Field(ge=1, le=12)
    species: str = Field(min_length=1)

class HoneyPredictResponse(BaseModel):
    species: str
    month: int
    predicted_honey_amount: float