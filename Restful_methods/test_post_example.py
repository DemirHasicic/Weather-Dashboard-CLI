
import requests

# This test sends a POST request to a mock API and checks if the response is successful and data is returned correctly
def test_post_user_creation():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Test Title",
        "body": "This is a test body.",
        "userId": 1
    }

    response = requests.post(url, json=payload)
    
    # Assert that the POST was successful
    assert response.status_code == 201, "Expected status code 201 for resource creation"
    
    json_response = response.json()

    # Assert that the response contains the sent data
    assert json_response["title"] == payload["title"]
    assert json_response["body"] == payload["body"]
    assert json_response["userId"] == payload["userId"]
