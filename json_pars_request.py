import requests

payload = {"name": "Vladimir"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
obj = response.json()
print(obj)
print(obj["answer"])