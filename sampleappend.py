test = open("/root/sample.txt",'a')
test.write("I am from Python Script 12435")
test.close()

test1 = open("/root/sample.txt",'r')
x = test1.read()
print (x)
test1.close()
