
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

print (f"Module: {module}, Grade: {grade}")

#for x in dict:
#    print (f"\t{modules['module']} : {results['results']}")
