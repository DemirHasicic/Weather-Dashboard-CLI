
import requests

def test_delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)

    assert response.status_code == 200 or response.status_code == 204
    print(f"DELETE Response Code: {response.status_code}")
