import csv
import time
f = open('/root/mydata.csv','r')
reader = csv.reader(f)
for row in reader:
	print (row)
	time.sleep(3)
f.close()

