
mystr = "welcome to looping"
num = len(mystr)-1
ans = []
ans1 = ''
while num >= 0:
	ans.append(mystr[num])
	ans1= ans1+mystr[num]
	num-=1
print ans
print ans1
print "Ending my program"
