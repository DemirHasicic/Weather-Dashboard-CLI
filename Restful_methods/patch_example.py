import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
patch_data = {
    "title": "Partially Updated Title"
}

response = requests.patch(url, json=patch_data)
print("Status Code:", response.status_code)
print("Response:", response.json())
