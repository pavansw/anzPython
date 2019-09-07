class Myclass:
	"This class is for basic Learning of python"
	num = 10
	def fun1(self):
		print ("Welcome msg from fun1 of Mycalss")

obj1 = Myclass()
obj2 = Myclass()

print (obj1.num**2)

print (obj1.__doc__)

obj1.fun1()

print (obj2.num**3)

print ("This is End of m code")

