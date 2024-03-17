import mysql.connector
from config import config as cfg

connection = mysql.connector.connect(
    host=cfg["host"],
    user = cfg["user"],
    password = cfg["password"]
)

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE WSAA")
mycursor.close()
connection.close()

