import mysql.connector
from config import config as cfg

mydb = mysql.connector.connect(
    host=cfg["host"],
    user = cfg["user"],
    password = cfg["password"],
    database = cfg["database"]
)

mycursor = mydb.cursor()

sql="create table student (id int auto_increment primary key, name varchar(255), age int)"
mycursor.execute(sql)

mycursor.close()
mydb.close()
