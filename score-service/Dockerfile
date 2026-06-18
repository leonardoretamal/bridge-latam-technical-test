FROM python:3.12-slim AS builder

WORKDIR /build

COPY pyproject.toml ./
COPY score_service ./score_service


RUN python -m pip install --upgrade pip \
    && python -m pip wheel --wheel-dir /wheels .

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /wheels /wheels
RUN python -m pip install --no-cache-dir /wheels/*.whl \
    && rm -rf /wheels

CMD ["uvicorn", "score_service.main:app", "--host", "0.0.0.0", "--port", "8080"]
