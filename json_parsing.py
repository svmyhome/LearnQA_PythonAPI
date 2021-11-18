import json

string_as_json = '{"answer": "Hello, Vladimir111"}'
obj = json.loads(string_as_json)
# print(obj)
# print(obj["answer"])

key = "answer   "

if key in obj:
    print(f"Ключ {key} = {obj[key]}")
else:
    print(f"Ключ {key} не найден")
