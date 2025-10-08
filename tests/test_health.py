# import os, requests

# BASE = os.getenv("API_BASE", "http://localhost:8000")

# def test_health_e2e():
#     r = requests.get(f"{BASE}/healthz", timeout=3)
#     assert r.status_code == 200
#     assert r.json().get("status") == "ok"