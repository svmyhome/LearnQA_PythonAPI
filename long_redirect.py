import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
for i in response.history:
    print(i.url)
    print(i.status_code)
print(response.status_code)
print(response.url)
