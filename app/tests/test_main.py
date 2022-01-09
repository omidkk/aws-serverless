from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_af_v1():
    response= client.post(f"/api/v1/flatten/af-v1", json={"input":[1.3,[2,[5,[6]]],[7],8]})
    assert response.status_code == 200
    assert response.json() == {"output": [1.3,2,5,6,7,8]}

def test_af_v2():
    response= client.post(f"/api/v1/flatten/af-v2", json={"input":[1.3,[2,[5,[6]]],[7],8]})
    assert response.status_code == 200
    assert response.json() == {"output": [1.3,2,5,6,7,8]}

