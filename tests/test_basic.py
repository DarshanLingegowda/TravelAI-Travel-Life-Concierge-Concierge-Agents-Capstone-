from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    r = client.get("/")
    assert r.status_code == 200

