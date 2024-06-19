import requests
import requests
import os

url = "https://api.elevenlabs.io/v2"

headers = {"xi-api-key": ""}

response = requests.request("GET", url, headers=headers)

print(response.text)

response = requests.request("GET", url, headers=headers)

print(response.text)