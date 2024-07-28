import requests

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)  # для GET используем params, а для POST используем data
print(response1.text)
print(response1.status_code)
print(response1.cookies)
print(dict(response1.cookies))
print(response1.headers)
print("-" * 10)
cookie_value = response1.cookies.get("auth_cookie")
cookie = {}
if cookie is not None:
    cookie.update({"auth_cookie": cookie_value})
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookie)
print(response2.text)
print(response2.status_code)
print(response2.request.headers)