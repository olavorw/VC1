import requests

url = "https://api.elevenlabs.io/v1/voices"

headers = {"xi-api-key": ""}

response = requests.request("GET", url, headers=headers)

print(response.text)