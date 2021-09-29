import requests

api_url = requests.get("http://localhost:8080/api/v1/nodes")
print(api_url)
api_url.json()
