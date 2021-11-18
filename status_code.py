import requests

response = requests.get("https://playground.learnqa.ru/api/check_type")  # для GET используем params, а для POST используем data
print(response.text)
print(response.status_code)
print("-" * 10)
response500 = requests.get("https://playground.learnqa.ru/api/get_500")  # для GET используем params, а для POST используем data
print(response500.text)
print(response500.status_code)
print("-" * 10)
response400 = requests.get("https://playground.learnqa.ru/api/something")  # для GET используем params, а для POST используем data
print(response400.text)
print(response400.status_code)
print("-" * 10)
response301 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)  # в случае allow_redirects=False не идем на редирект и будут данные только 1-го запроса
print(response301.text)
print(response301.status_code)
print("-" * 10)
response301 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)  # По умолчанию True, в случае allow_redirects=True  идем на редирект и получаем данные из редиректа,
response301_0 = response301.history[0]
response301_1 = response301
print(response301_0.status_code)
print(response301_0.url)
print(response301_1.status_code)
print(response301_1.url)
print(response301.text)