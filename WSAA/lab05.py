import requests
import json

from config import config as cfg
url = 'https://api.github.com/repos/PeeBs68/aprivateone'
#apikey = cfg["html2pdfkey"]
apikey = cfg["githubkey"]

print (apikey)

response = requests.get(url, auth=('token',apikey))
repoJSON = response.json()

filename = "aprivateone.txt"
with open(filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)
