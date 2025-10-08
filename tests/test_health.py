from fastapi.testclient import TestClient
from app.main import app

def test_health_unit():
    c = TestClient(app)
    r = c.get("/healthz")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"