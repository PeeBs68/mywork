import mysql.connector
from config import config as cfg

db = mysql.connector.connect(
    host=cfg["host"],
    user = cfg["user"],
    password = cfg["password"],
    database = cfg["database"]
)
print("Connected")

cursor = db.cursor()

sql = "delete from student where id = %s"
values = (1,)
cursor.execute(sql, values)
db.commit()

print("One record deleted")

cursor.close()
db.close()

print("Connection Closed")