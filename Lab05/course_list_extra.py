# lab5.4 create a dict by reading in a student name, courses and grades
# break when the module entered is blank

student_file = {}
student_file2 = {"Name" : [], "Module" : [], "Grade" : []}

person1 = input("Enter a name: ")
#student_file["Name"]=person1
student_file2["Name"]=person1
module1 = "temp" #dummy just to make the 1st loop run
# Finish if nothing is entered for module
while len(module1)!= 0:
    module1 = input("Enter a module: ")
    if len(module1)>0:
#        student_file["Module"]=module1
        student_file2["Module"].append(module1)
        grade1 = input("Enter a grade: ")
#        student_file["Grade"]=grade1
        student_file2["Grade"].append(grade1)
#print (student_file)
#print (student_file2)

print(f"Name: {student_file2['Name']}")

#print (f"Module: {student_file2['Module']}")

#print (f"\t{student_file2['Module']} : {student_file2['Grade']}")
for x in student_file2["Module"]:
    print (f"Module :\t{student_file2['Module']} Grade : {student_file2['Grade']}")

for course in student_file2["Module"]:
    print (f"\t{student_file2['Module']} : {student_file2['Grade']}")