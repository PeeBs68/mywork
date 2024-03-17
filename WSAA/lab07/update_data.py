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

sql = "update student set name = %s, age = %s where id = %s"
values = ("Alan", 110, 3)
cursor.execute(sql, values)
db.commit()

print("Record Updated,")

cursor.close()
db.close()

print("Connection Closed")