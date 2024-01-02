from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
            "code": 200, 
            "message": "Welcome to API Inference Playground of Text Classification"
        }