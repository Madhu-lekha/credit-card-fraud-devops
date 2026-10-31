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

    assert b"Potentially Fraudulent" in response.data


def test_legitimate_transaction():

    client = app.test_client()

    response = client.post(
        "/predict",
        data={"amount": "500"}
    )

    assert b"Legitimate Transaction" in response.data