import os
os.environ.setdefault("DATABASE_URL","postgresql+psycopg://test:test@localhost:5432/test")
os.environ.setdefault("JWT_SECRET_KEY","test-only-secret-key-that-is-long-enough-for-tests")
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health_endpoint():
    response=client.get("/health")
    assert response.status_code==200
    assert response.json()["status"]=="ok"
def test_employee_directory_requires_authentication():
    assert client.get("/employees").status_code==401
def test_current_user_requires_authentication():
    assert client.get("/auth/me").status_code==401
