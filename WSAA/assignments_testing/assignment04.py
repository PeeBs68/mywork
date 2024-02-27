# assignment04-github.py

# Author: Phelim Barry

# Purpose: Read a file from a repo, make changes to the file and then push it back to the repo

import requests
from config import config as cfg
from github import Github

apikey = cfg["githubkey"]
g = Github(apikey)

repo = g.get_repo("PeeBs68/mywork")

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

response = requests.get(urlOfFile)
originalcontents = response.text

original_str = "two"
new_str = "bye there"
newcontents = originalcontents.replace(original_str, new_str)

gitHubResponse=repo.update_file(fileInfo.path,"File Update", newcontents,fileInfo.sha)
print (gitHubResponse)

