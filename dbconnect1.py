import pymysql

db = pymysql.connect("localhost","pavan","redhat","TESTDB")

cursor = db.cursor()

cursor.execute("SELECT * from test;")

data = cursor.fetchall()

print (data)

db.close()
