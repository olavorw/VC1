import requests
import requests
import os

url = "https://api.elevenlabs.io/v1/voices"

headers = {"xi-api-key": "YOUR_API_KEY"}

response = requests.request("GET", url, headers=headers)

print(response.text)

response = requests.request("GET", url, headers=headers)

print(response.text)