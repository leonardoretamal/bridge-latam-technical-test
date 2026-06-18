from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DimensionScores(BaseModel):
    """Validated score values for the five company health dimensions."""

    governance: float = Field(ge=0.0, le=100.0)
    innovation: float = Field(ge=0.0, le=100.0)
    operations: float = Field(ge=0.0, le=100.0)
    finance: float = Field(ge=0.0, le=100.0)
    sustainability: float = Field(ge=0.0, le=100.0)

    model_config = ConfigDict(extra="forbid")


class ScoreRequest(BaseModel):
    company_id: UUID
    dimensions: DimensionScores

    model_config = ConfigDict(extra="forbid")


class ScoreResponse(BaseModel):
    company_id: str
    composite_score: float
    grade: str
    dimension_scores: DimensionScores
    computed_at: datetime

    model_config = ConfigDict(extra="forbid")
