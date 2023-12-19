import requests
import json

url = 'https://web-production-6c79.up.railway.app/send'

data = {'user': 'thomas', 'group_name': 'S.T??.E.R'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)