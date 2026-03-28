## Connect to FakeStoreAPI
import requests

response_API = requests.get("https://fakestoreapi.com/products/1")
print(response_API.json())