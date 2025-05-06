import requests

url = "https://jsonplaceholder.typicode.com/posts"

head_response = requests.head(url)
print("HEAD Status Code:", head_response.status_code)
print("HEAD Headers:", head_response.headers)

options_response = requests.options(url)
print("OPTIONS Status Code:", options_response.status_code)
print("OPTIONS Headers:", options_response.headers)
