import requests
import json

command = {
  "command": "getTransactionsToApprove",
  "depth": 3
}

stringified = json.dumps(command)

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

request = requests.post(url="http://localhost:14265", data=stringified, headers=headers)
returnData = request.text

jsonData = json.loads(returnData)

print(jsonData)
