import json

import requests
import time


response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
data_response = json.loads(response.text)
data_token = data_response["token"]
# print(type(data_response))
print(f"Token is: {data_response}")
payload = {"token": data_token}
status = ""
while "Job is ready" != status:
    time.sleep(2)
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    data_response_status = json.loads(response.text)
    status = data_response_status["status"]
    print(status)
print(data_token)
print(response.text)
