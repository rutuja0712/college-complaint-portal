import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app, complaints


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        complaints.clear()
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_get_complaints(client):
    response = client.get("/api/complaints")

    assert response.status_code == 200
    assert response.get_json() == []


def test_add_complaint(client):
    complaint = {
        "name": "Rutuja",
        "category": "Infrastructure",
        "details": "Projector is not working."
    }

    response = client.post(
        "/api/complaints",
        json=complaint
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["message"] == "Complaint submitted successfully"
    assert data["complaint"]["name"] == "Rutuja"
    assert data["complaint"]["category"] == "Infrastructure"


def test_invalid_complaint(client):
    complaint = {
        "name": "",
        "category": "Infrastructure",
        "details": ""
    }

    response = client.post(
        "/api/complaints",
        json=complaint
    )

    assert response.status_code == 400
