import pymysql

db = pymysql.connect("localhost","pavan","redhat","TESTDB")

cursor = db.cursor()

test = "INSERT INTO test values ('sample',3456);"

cursor.execute(test)

cursor.execute("commit;")

db.close()
