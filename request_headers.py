import requests

headers = {"some_header": "111111111111111111111111111"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)  # для GET используем params, а для POST используем data
print(response.text)
print(response.headers)

