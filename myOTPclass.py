import random
import string

testGlobal = 'pavan'

class Myclass:
	result = ""
	"This class is for OTP operations"
	def otp(self,x):
		#result = ""
		for var in random.sample(string.printable,x):
			self.result = self.result+var
		print ("Global variable print from calss: ",testGlobal)
		return self.result

num = int(input("Enter desired legth of OTP: "))

obj1 = Myclass()

print (obj1.otp(num))

print ("This is End of m code")

