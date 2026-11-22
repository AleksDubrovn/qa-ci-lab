import os
import requests



BASE_URL = os.getenv(
    "BASE_URL",
    "https://jsonplaceholder.typicode.com",
)

def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1",timeout=10)
    assert response.status_code == 200
    assert response.json()["id"] == 1
