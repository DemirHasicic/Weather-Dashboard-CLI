import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "New post",
    "body": "Content of the new post",
    "userId": 1
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
