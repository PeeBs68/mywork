# lab7.5 - additions to lab 6

import json

FILENAME = "student_list.txt"

def doAdd(students):
    currentStudent = {}
    currentStudent ["name"] = input("Enter a name: ")
    currentStudent ["modules"] = readModules()
    students.append(currentStudent)

def displayModules(modules):
    print (f"\tName  \t Grade")
    for module in modules:
        print (f'\t{ module["name"]} \t { module["grade"]}')

def doView(students):
    for currentStudent in students:
        print (currentStudent["name"])
        displayModules(currentStudent["modules"])

def doSave(students):
    print ("Saving to a file...")
    with open(FILENAME, 'wt') as f:
        json.dump(students, f)

def doOpen(students):
    with open(FILENAME, 'rt') as f:
        students = json.load(f)
        doView(students)
        print (students)
        return students

def readModules():
    #create another list
    modules = []
    module_name = input("Enter a module: ")
    while len(module_name) > 0:
        #create a dictionary for module which will have module and grade
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("Enter a grade: "))
        #now append the dict into the list
        modules.append(module)
        module_name = input("Enter anther module: ")

    return modules

def menu():
    print("Here are your options")
    print (students)
    print("\t(a) Add new student")
    print("\t(v) View Students")
    print("\t(s) Save Students")
    print("\t(l) Load Students")
    print("\t(q) Quit")
    item = (input("Type one letter (a,v,s,l,q):  "))

    return item

# the actual code
students = []
item = menu()
while (item != "q"):
    if item == "a":
        doAdd(students)
    elif item == "v":
        doView(students)
    elif item == "s":
        doSave(students)
    elif item == "l":
        doOpen(students)
    elif item != "q":
        print ("It needs to be either a,v,s,l,q")
    item = menu()
print (f"You choose: {item} to quit")
