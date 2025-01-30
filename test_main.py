from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello There!"}

def test_hello_func():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_another_func():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Another random route added!"}


