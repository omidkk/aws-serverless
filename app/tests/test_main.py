from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_resource():
    response_auth = client.get(f"/")
    assert response_auth.status_code == 200


def test_af_v1():
    response= client.post(f"/api/v1/flatten/af-v1",
                                json=[1.3,[2,[5,[6]]],[7],8])
    assert response.status_code == 200
    assert response.json() == [1.3,2,5,6,7,8]

def test_af_v2():
    response= client.post(f"/api/v1/flatten/af-v2",
                          json=[1.3,[2,[5,[6]]],[7],8])
    assert response.status_code == 200
    assert response.json() == [1.3,2,5,6,7,8]

