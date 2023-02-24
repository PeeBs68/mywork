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
print(f"Student: {student_file['name']}")
for course in student_file["Results"]:
    print (f"\t{course['Course']} : {course['Grade']}")
