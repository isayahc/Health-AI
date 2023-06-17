import file from .json

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()

response.smile = "CC8"
response.weights = "colors"
response.toxicityscore = "4"

