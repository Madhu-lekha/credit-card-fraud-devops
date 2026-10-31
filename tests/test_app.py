import sys
from pathlib import Path

# Add the project root directory to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_fraud_transaction():
    client = app.test_client()

    response = client.post(
        "/predict",
        data={"amount": "15000"}
    )

    assert response.status_code == 200
    assert b"Potentially Fraudulent" in response.data


def test_legitimate_transaction():
    client = app.test_client()

    response = client.post(
        "/predict",
        data={"amount": "500"}
    )

    assert response.status_code == 200
    assert b"Legitimate Transaction" in response.data
