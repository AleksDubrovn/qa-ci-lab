import requests


def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=10)
    assert response.status_code == 200
    assert response.json()["id"] == 1
