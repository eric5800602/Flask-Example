import requests
import json

url = 'http://localhost:6969/send'

data = {'user': 'thomas', 'group_name': 'S.T??.E.R'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)