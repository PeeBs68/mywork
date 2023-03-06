# lab6.6 - add 6.3 and 6.4 and 6.5 together

def doAdd(students):
    currentStudent = {}
    currentStudent ["name"] = input("Enter a name: ")
    currentStudent ["modules"] = readModules()
    students.append(currentStudent)

def doView():
    print("Viewing")
    print(students)

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
    print("\t(a) Add new student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    item = (input("Type one letter (a/v/q):  "))

    return item

# the actual code
students = []
item = menu()
while (item != "q"):
    if item == "a":
        doAdd(students)
    elif item == "v":
        doView()
    elif item != "q":
        print ("It needs to be either a,v,q")
    item = menu()
print (f"You choose: {item} to quit")
