from json.decoder import JSONDecodeError
import requests


response = requests.get("https://playground.learnqa.ru/api/get_text")  # get_text ендпоинт возвращающий текст, а не json, поэтому так и отрпжается.
print(response.text)

try:
    obj = response.json()
    print(obj["answer"])
except JSONDecodeError:
    print("Response is not JSON format")