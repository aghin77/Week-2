import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print("Status Code:", response.status_code)
print("Response Data:", response.json())