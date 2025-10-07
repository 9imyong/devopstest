import requests


# Simple smoke test when container is running locally
# Run: `docker compose up -d` before executing this test


def test_health_local():
    r = requests.get('http://localhost:8000/healthz', timeout=2)
    assert r.status_code == 200
    assert r.json().get('status') == 'ok'