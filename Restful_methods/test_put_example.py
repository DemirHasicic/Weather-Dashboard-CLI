import requests

def test_put_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    updated_data = {
        "id": 1,
        "title": "Updated Title",
        "body": "This is the updated content of the post.",
        "userId": 1
    }

    response = requests.put(url, json=updated_data)

    # Assertions to validate the response
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["title"] == updated_data["title"]
    assert json_data["body"] == updated_data["body"]
    assert json_data["userId"] == updated_data["userId"]
