# lab5.4 create a dict by reading in a student name, courses and grades
# break when the module entered is blank

student_file = {}

person1 = input("Enter a name: ")
student_file["Name"]=person1
module1 = "temp" #dummy just to make the 1st loop run
# Finish if nothing is entered for module
while len(module1)!= 0:
    module1 = input("Enter a module: ")
    if len(module1)>0:
        student_file["Module"]=module1
        grade1 = input("Enter a grade: ")
        student_file["Grade"]=grade1
print (student_file)


#while module1 != "":
#    module1 = input("Enter a module: ")
#    student_file["Module"]=module1
#    grade1 = input("Enter a grade: ")
#    student_file["Grade"]=grade1

#print (student_file)

#    "Name" : "", 
#    "Results" : [{
#        "Course" : "",
#        "Grade" : 0}
#    ]
#}


#student_file = {
#    "name" : "Mary", 
#    "Results" : [{
#        "Course" : "Programming",
#        "Grade" : 99 },
#        {"Course" : "Scripting",
#        "Grade" : 77
#        }
#    ]
#}
#print(f"Student: {student_file['name']}")
#for course in student_file["Results"]:
#    print (f"\t{course['Course']} : {course['Grade']}")
