import requests
import requests
import os

url = "https://api.elevenlabs.io/v2"

headers = {"xi-api-key": "92bf014d900ce7ef6b1a83e7e864f9a8"}

response = requests.request("GET", url, headers=headers)

print(response.text)

response = requests.request("GET", url, headers=headers)

print(response.text)