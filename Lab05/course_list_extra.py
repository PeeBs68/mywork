# lab5.4 create a dict by reading in a student name, courses and grades
# break when the module entered is blank

student_file = {
    "name" : "Mary", 
    "Results" : [{
        "Course" : "Programming",
        "Grade" : 99 },
        {"Course" : "Scripting",
        "Grade" : 77
        }
    ]
}
student_file = {}
student_file2 = {
    "Name" : [],
    "Results" : [{ 
        "Module" : [], 
        "Grade" : []
        }
    ]
}

print (student_file2)
person1 = input("Enter a name: ")
#student_file["Name"]=person1
student_file2["Name"]=person1
module1 = "temp" #dummy just to make the 1st loop run
# Finish if nothing is entered for module
while len(module1)!= 0:
    module1 = input("Enter a module: ")
    if len(module1)>0:
#        student_file["Module"]=module1
        student_file2["Results"].append(module1)
        grade1 = input("Enter a grade: ")
#        student_file["Grade"]=grade1
        student_file2["Results"].append(grade1)
#print (student_file)
#print (student_file2)

print(f"Name: {student_file2['Name']}")
print(f"Results: {student_file2['Results']}")
print(f"Grade: {student_file2['Grade']}")
print(f"Results: {student_file2['Results']['Module']}")
print(f"Results: {student_file2['Grade']}")
#print (f"Module: {[student_file2.Module]['Results']}")

#print (f"\t{student_file2['Module']} : {student_file2['Grade']}")
#for x in student_file2["Results"]:
#    print (f"Module :\t{student_file2['Results']} Grade : {student_file2['Results']}")

#for course in student_file2["Module"]:
#    print (f"\t{student_file2['Module']} : {student_file2['Grade']}")