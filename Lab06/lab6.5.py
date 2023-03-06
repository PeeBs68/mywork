#Lab6.5 which adds the entering the modules in readModules

#This part from lab6.4
#create a list
students = []

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

def doAdd(students):
    currentStudent = {}
    currentStudent ["name"] = input("Enter a name: ")
    currentStudent ["modules"] = readModules()

    students.append(currentStudent)

doAdd(students)
#add another
doAdd(students)
print (students)