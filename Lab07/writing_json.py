#lab7 json - writing

import json

FILENAME = "json_text.txt"

dict = {}
dict["name"] = input("Enter a name: ")
dict["age"] = int(input("Enter an age: "))
print (dict)

#1 - assume the file exists
with open(FILENAME, 'wt') as f:
    json.dump(dict, f)
