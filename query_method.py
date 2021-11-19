import json

import requests

met_obj = ["https://playground.learnqa.ru/ajax/api/compare_query_type", "https://playground.learnqa.ru/ajax/api/compare_query_type", "https://playground.learnqa.ru/ajax/api/compare_query_type", "https://playground.learnqa.ru/ajax/api/compare_query_type"]
met_elem ='{ "items":[ { "method":"GET"}, { "method":"POST"}, { "method":"PUT"}, { "method":"DELETE" }]}'
# print(type(met_elem))
obj = json.loads(met_elem)
for i in met_obj:
    for j in obj["items"]:
        r1 = requests.get(i, params = j)
        r2 = requests.post(i, data = j)
        r3 = requests.put(i, data = j)
        r4 = requests.delete(i, data = j)
        print("-" * 10, j, "-" * 10)
        print("GET", r1.text)
        print("POST", r2.text)
        print("PUT", r3.text)
        print("DELETE", r4.text)
# print(type(obj))
# print(obj)
# print(obj["response"]["items"][0])
# s2 = obj["response"]["items"][0]
# s1 = met_obj[0]
# s3 = s1, s2
# r1 = requests.get(s1, s2)
# print(s1)
# print(s2)
# print(s3)
# print(r1.text)
# s1 = met_obj[0]
# r1 = requests.get(s1, params={'method': 'GET'})
# print(r1.text)

# print(met_obj[0])
# print(met_obj[1])
# print(met_elem[1])
# print("-" * 10, "GET", "-" * 10)
# response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
# print(response.status_code)
# print(response.url)
# print(response.text)
# print("-" * 10, "post", "-" * 10)
# response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
# print(response.status_code)
# print(response.url)
# print(response.text)
# print("-" * 10, "put", "-" * 10)
# response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
# print(response.status_code)
# print(response.url)
# print(response.text)
# print("-" * 10, "DEL", "-" * 10)
# response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})
# print(response.status_code)
# print(response.url)
# print(response.text)
# print("-" * 10, "HEAD", "-" * 10)
# response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
# print(response.status_code)
# print(response.url)
# print(response.text)
# print("-" * 10, "CICLE", "-" * 10)
