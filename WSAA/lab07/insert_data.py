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

sql = "insert into student (name, age) values (%s, %s)"
values = ("Mary", 21)
cursor.execute(sql, values)
db.commit()

print("One record inserted, ID", cursor.lastrowid)

cursor.close()
db.close()

print("Connection Closed")