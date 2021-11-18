import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

print(json_text)
print(type(json_text))
print("*" * 50)
obj = json.loads(json_text)
print(obj)
print(type(obj))
print("*" * 50)
print(obj["messages"])
print(type(obj["messages"]))
print("*" * 50)
print(obj["messages"][1])
print(type(obj["messages"][1]))
print("*" * 50)
print(obj["messages"][1]["timestamp"])
print(type(obj["messages"][1]["timestamp"]))
print("*" * 50)
for i in obj["messages"]:
    print(i["message"], i["timestamp"],)