# Company Health Score

This repository contains a FastAPI score service and a Nuxt dashboard widget for the technical interview task.

## Backend

```bash
cd score-service
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
pytest
uvicorn score_service.main:app --host 0.0.0.0 --port 8080
```

## Frontend

```bash
npm install
$env:NUXT_SCORE_SERVICE_URL = "http://localhost:8080"
npm run dev
```

The Nuxt widget calls `/api/score`, and the server route proxies the request to the private `scoreServiceUrl` runtime config value.
