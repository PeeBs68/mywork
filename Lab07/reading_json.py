#lab7 json - reading

import json

FILENAME = "json_text.txt"

with open(FILENAME, 'rt') as f:
    dict = json.load(f)

print (dict["name"], dict ["age"])

print (dict)
