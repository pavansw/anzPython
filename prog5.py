
mystr = "welcome to looping"
num = 0
ans1 = ''
while num < len(mystr):
	if num%2==0:
		ans1= ans1+mystr[num]
	num+=1
print ans1
print "Ending my program"
