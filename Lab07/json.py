#lab7 json

import json

FILENAME = "json.txt"

dict = {}
module = {}
dict["name"] = int(input("Enter a name: "))
dict["age"] = int(input("Enter an age: "))

#1 - assume the file exists
with open(FILENAME, 'r') as f:
    json.dump(dict, f)

#2 - assume the file doesn't exist
#f = open(FILENAME, "x")