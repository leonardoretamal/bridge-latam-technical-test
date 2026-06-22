from httpx import AsyncClient

from score_service.scoring import calculate_composite_score, classify_grade

VALID_PAYLOAD = {
    "company_id": "4c9c1287-9786-4b4d-8c33-dba6c9c4d86f",
    "dimensions": {
        "governance": 80,
        "innovation": 70,
        "operations": 65,
        "finance": 75,
        "sustainability": 72,
    },
}


async def test_score_returns_computed_result(client: AsyncClient) -> None:
    response = await client.post("/score", json=VALID_PAYLOAD)

    assert response.status_code == 200
    body = response.json()
    assert body["company_id"] == VALID_PAYLOAD["company_id"]
    assert body["composite_score"] == 72.8
    assert body["grade"] == "B"
    assert body["dimension_scores"] == {
        "governance": 80.0,
        "innovation": 70.0,
        "operations": 65.0,
        "finance": 75.0,
        "sustainability": 72.0,
    }
    assert body["computed_at"].endswith("Z")


async def test_score_rejects_out_of_range_dimension(client: AsyncClient) -> None:
    payload = VALID_PAYLOAD | {"dimensions": VALID_PAYLOAD["dimensions"] | {"finance": 101}}

    response = await client.post("/score", json=payload)

    assert response.status_code == 422


async def test_score_rejects_missing_dimension(client: AsyncClient) -> None:
    dimensions = VALID_PAYLOAD["dimensions"].copy()
    del dimensions["sustainability"]
    payload = VALID_PAYLOAD | {"dimensions": dimensions}

    response = await client.post("/score", json=payload)

    assert response.status_code == 422


async def test_score_rejects_invalid_company_id(client: AsyncClient) -> None:
    payload = VALID_PAYLOAD | {"company_id": "not-a-uuid"}

    response = await client.post("/score", json=payload)

    assert response.status_code == 422


def test_calculate_composite_score_is_pure() -> None:
    assert calculate_composite_score(VALID_PAYLOAD["dimensions"]) == 72.8


def test_classify_grade_boundaries() -> None:
    assert classify_grade(85) == "A"
    assert classify_grade(70) == "B"
    assert classify_grade(55) == "C"
    assert classify_grade(54.9) == "D"
