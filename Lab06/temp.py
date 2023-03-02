#for playing around with lab06

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

doAdd()