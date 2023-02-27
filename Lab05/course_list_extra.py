# lab5.4 create a dict by reading in a student name, courses and grades
# break when the module entered is blank

student_file2 = {
    "Name" : "", 
    "Results" : [{
        "Course" : "",
        "Grade" : "",
        "Course" : ""}
    ]
}
person1 = input("Enter a name: ")
student_file2["Name"]=person1
course1 = "temp" #dummy just to make the 1st loop run
# Finish if nothing is entered for module
while len(course1)!= 0:
    course1 = input("Enter a module: ")
    if len(course1)>0:
        student_file2["Results"].append(course1)
        grade1 = input("Enter a grade: ")
        student_file2["Results"].append(grade1)
print (student_file2)

print(f"Student: {student_file2['Name']}")

for course in student_file2["Results"]:
    print (f"\t{course['Course']} : {course['Grade']}")

