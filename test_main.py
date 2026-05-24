from fastapi.testclient import TestClient
from main import app

# Create a test client that talks to your API
client = TestClient(app)


def test_root():
    # Test that the root endpoint returns 200 and the right message
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI is working"}


def test_ask():
    # Test that the /ask endpoint receives a question and responds
    response = client.post("/ask", json={"text": "What is a clinical trial?"})
    assert response.status_code == 200
    assert "you_asked" in response.json()
