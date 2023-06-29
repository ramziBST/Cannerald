import requests
from payloadCollection import PayloadCollection
import json
import base64

url = 'https://werk-fraubrunnen.onlinezuko.ch/rpc/'
payload = {
  "method": "eAccess.getModel",
  "params": [
    "AccessPointPropertyData",
    {},
    []
  ],
  "id": 2,
  "jsonrpc": "2.0"

}
credentials = f'{PayloadCollection.username}:{PayloadCollection.password}'
auth_header = 'Basic ' + base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

headers = {
    'Content-Type': 'application/json-rpc; charset=utf-8',
    'Authorization': auth_header,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',

        }
response = requests.post(url, headers=headers, data=json.dumps(payload,))
if response.status_code == 200:
    # Request was successful
    print('Request successful.')
    print('Response:', response.text)
else:
    # Request failed
    print('Request failed with status code:', response.status_code)
