import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

response = requests.get(url)
data = response.json()
print(response) #200 is good

with open("cso.json", "wt") as fp:
    print(json.dumps(data), file=fp)
