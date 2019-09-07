import random
import string
in1 = int(input("Enter length of OTP you want: "))
def otpGenerator(x):
	ans = ''
	for var in random.sample(string.printable,x):
		ans=ans+var
	return ans

test = otpGenerator(in1)
print ("OTp is :",test)

