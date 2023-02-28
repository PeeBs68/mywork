
dict = {}
results = {}
modules = []
name = input("Enter a name: ")
while name != "":
    module = input ("Enter a module: ")
    if module == "stop":
        break
    else:
        modules.append(module)
        grade = input("Enter a grade: ")
        results.update({"Course: " + module : "Grade: " + grade})
dict.update({name:results})
print (dict)

print(f"Student: {name}")

for x in modules:
    print (f"\tModule: {module}, Grade: {grade}")

