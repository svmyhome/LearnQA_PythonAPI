import requests

payload = {"name": "Vladimir"}
response = requests.get("https://playground.learnqa.ru/api/check_type", params=payload)  # для GET используем params, а для POST используем data
response1 = requests.post("https://playground.learnqa.ru/api/check_type", data=payload)  # для GET используем params, а для POST используем data
print(response.text)
print(response1.text)

