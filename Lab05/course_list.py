# lab5.4 create a dict for 1 student name, courses and grades

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
