from fastapi.testclient import TestClient
from session_11.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI API!"}

def test_create_item_success():
    response = client.post("/items/", json={"name": "Test Item", "price": 19.99})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Test Item", "price": 19.99}}
