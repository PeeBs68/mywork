dict = {}
results = {}
modules = []
grades = []

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

print(f"Student: {name}")
print (len(modules))

for x in range(len(modules)):
    print (f"\tModule: {modules[x]}, Grade: {grades[x]}")
