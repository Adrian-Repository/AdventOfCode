import requests
data = {"a_key": "a_value"}

url = "https://www.hackthebox.eu/api/invite/generate"

response = requests.post(url, data)

print(response)