# assignment04-github.py

# Author: Phelim Barry

# Purpose: Read a file from a repo, make changes to the file and then push it back to the repo

import requests
import json
import base64
from config import config as cfg
from requests.auth import HTTPBasicAuth  # For basic authentication

url = "https://raw.githubusercontent.com/PeeBs68/mywork/main/WSAA/assignments_testing/"
filename = "temp.txt"
geturl = url+filename
#fullurl = "https://raw.githubusercontent.com/PeeBs68/mywork/main/WSAA/assignments_testing/temp.txt"
print(geturl)

response = requests.get(geturl)
data = response.text
print(data)

original_name = "new"
new_name = "one"
data = data.replace(original_name, new_name)
print(data)

with open(filename, 'w') as fp:
    fp.write(data)

apikey = cfg["githubkey"]
# posting

url = "https://api.github.com/repos/PeeBs68/mywork/contents/WSAA/assignments_testing/"
filename = "temp.txt"
posturl = url+filename
apikey = cfg["githubkey"]

#get sha value: https://stackoverflow.com/questions/75327473/how-do-you-push-files-to-a-github-repo-in-python
response = requests.get(posturl)
sha = response.json()['sha']
#print(sha)
posturl = posturl+"/"+sha

aa=open(filename,'r').read()
print(aa)
text= base64.b64encode(aa.encode("utf-8"))
api="https://api.github.com/repos/PeeBs68/mywork/contents/WSAA/assignments_testing/temp.txt"
headers = {
    "Authorization": f'''Bearer {apikey}''',
    "Content-type": "application/vnd.github+json"
}
data = {
    "message": "File Update2",
    "content": text.decode("utf-8"),
    "sha": sha
}

r = requests.put(api, headers=headers, json=data)
print(r.text)