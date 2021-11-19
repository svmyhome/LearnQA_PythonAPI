import json
met_elem ='{ "items":[ { "method":"GET"}, { "method":"POST"}, { "method":"PUT"}, { "method":"DELETE" }]}'
obj = json.loads(met_elem)
for i in obj["items"]:
 i['method1'] = "HEAD"
print(obj)
new_json = json.dumps(obj, indent=2)
print(new_json)

with open('my.json', 'w') as file:
   json.dump(obj, file, indent=2)
