#Lab6.4

#had to copy Andres - my list/dict was a mess!
#create a list just for the names
students = []

#temp - doesn't do anything for noe
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