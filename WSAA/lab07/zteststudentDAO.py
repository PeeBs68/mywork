from zstudentDAO import studentDAO

#create student
latestid = studentDAO.create(('mark', 45))

#find by ID
result = studentDAO.findbyID(latestid);
print(result)

#update record
studentDAO.update(("Fred", 51, latestid))
result = studentDAO.findbyid(latestid);
print(result)

#get all
allStudents = studentDAO.getAll()
for student in allStudents:
    print (student)

#delete
#studentDAO.delete(latestid)

