#! /usr/bin/python3

import requests

response = requests.get('http://0.0.0.0:8080/api/flights/v1/health')

print(response.status_code)
print(response.text)
dic = response.json()
print(dic['message'])
