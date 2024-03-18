import mysql.connector

class studentDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        # use a config file here
        self.host = "localhost"
        self.user = "root"
        self.password = "rootroot"
        self.database = "wsaa"

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql = "insert into student (name, age) values (%s, %s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from student"
        cursor.execute(sql)
        self.closeAll()

    