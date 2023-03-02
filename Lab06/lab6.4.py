# Lab06.3
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