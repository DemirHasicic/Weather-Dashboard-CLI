import requests

def test_patch_example():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    patch_data = {
        "title": "patched title"
    }

    response = requests.patch(url, json=patch_data)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["title"] == "patched title"
