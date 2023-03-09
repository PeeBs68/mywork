#for playing around with lab06

#dict = {}
#results = {}
#modules = []
#grades = []

#def doAdd():
#    name = input("Enter a name: ")
#    module = "temp" #Used just to get the loop running - must find a better way for this
    # Finish if nothing is entered for module
#    while len(module)!= 0:
#        module = input ("Enter a module: ")
#        if len(module)>0:
#            modules.append(module)
#            grade = input("Enter a grade: ")
#            grades.append(grade)
#            results.update({"Course: " + module : "Grade: " + grade})
#    dict.update({name:results})
#    print (dict)

#doAdd()

'''#create a list
students = []

def readModules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent ["name"] = input("Enter a name: ")
    currentStudent ["modules"] = readModules()

    students.append(currentStudent)

doAdd(students)
#add another
doAdd(students)
print (students)

#Original 6.4 stuff
# Lab06.4
# Adding students using the doAdd function
dict = {}
results = {}
modules = []
grades = []

def doAdd():
    name = input("Enter a name: ")
    module = "temp" #Used just to get the loop running - must find a better way for this
    # Finish if nothing is entered for module
    while len(module)!= 0:
        module = input ("Enter a module: ")
        if len(module)>0:
            modules.append(module)
            grade = input("Enter a grade: ")
            grades.append(grade)
            results.update({"Course: " + module : "Grade: " + grade})
    dict.update({name:results})
    print (dict)


def doView():
    print("Viewing")

def menu():
    print("Here are your options")
    print("\t(a) Add new student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    item = (input("Type one letter (a/v/q):  "))

    return item

item = menu()
while (item != "q"):
    if item == "a":
        doAdd()
    elif item == "v":
        doView()
    elif item != "q":
        print ("It needs to be either a,v,q")
    item = menu()
print (f"You choose: {item} to quit")
'''

number = float(input("enter a number : "))
apprx_root = number * 0.5
print (apprx_root)

more_accurate = 0.5 * (apprx_root + number/apprx_root)
print (more_accurate)


while (number != more_accurate*more_accurate):
    more_accurate = 0.5 * (more_accurate + number/more_accurate)
    print (more_accurate, apprx_root)

print (more_accurate)