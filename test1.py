import requests

payload = {"name": "Vladimir111"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)