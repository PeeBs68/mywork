# assignment04-github.py

# Author: Phelim Barry

# Purpose: Read a file from a repo, make changes to the data and then push the file back to the repo

import requests
from config import config as cfg
from github import Github

apikey = cfg["githubkey"]
g = Github(apikey)

repo = g.get_repo("PeeBs68/mywork")
fileinfo = repo.get_contents("test.txt")
fileurl = fileinfo.download_url

response = requests.get(fileurl)
originalcontents = response.text

original_str = "three"
new_str = "bye again"
newcontents = originalcontents.replace(original_str, new_str)

response=repo.update_file(fileinfo.path,"File Update", newcontents,fileinfo.sha)
print (response)

