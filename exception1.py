import sys
print ("Trying some err and exception")

try:
	number = int(input("Enter a no: "))

except ValueError:
	print ("Ops.. Numbers only")
	sys.exit()

print ("you entered ", number)
