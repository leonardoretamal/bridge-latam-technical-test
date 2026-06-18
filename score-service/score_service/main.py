import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import FastAPI

from score_service.config import Settings
from score_service.models import ScoreRequest, ScoreResponse
from score_service.scoring import calculate_composite_score, classify_grade

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logging.basicConfig(level=settings.log_level.upper())
    logging.getLogger(__name__).info("Score service started")
    yield
    logging.getLogger(__name__).info("Score service stopped")


app = FastAPI(title="Company Health Score API", version="0.1.0", lifespan=lifespan)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/score", response_model=ScoreResponse)
async def score_company(payload: ScoreRequest) -> ScoreResponse:
    dimension_scores = payload.dimensions.model_dump()
    composite_score = calculate_composite_score(dimension_scores)

    return ScoreResponse(
        company_id=str(payload.company_id),
        composite_score=composite_score,
        grade=classify_grade(composite_score),
        dimension_scores=payload.dimensions,
        computed_at=datetime.now(UTC),
    )
