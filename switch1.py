def my_circle(r):
	return 3.14*r*r

def my_square(s):
	return s**2

def my_rectange(b,h):
	return b*h/2

choice = int(input("enter 1. Area of circle \n 2. Area of square \n 3. Area of rectangle \n 0. To exit"))

if choice==1:
	var = eval(input("What is r? "))
	print ("Area of Circle is : ",my_circle(var))
elif  choice==2:
	var1 = eval(input("What is s? "))
	print ("Area of Square is : ",my_square(var1))
elif  choice==3:
	var2 = eval(input("What is b? "))
	var3 = eval(input("What is h? "))
	print ("Area of rectangle is : ",my_rectange(var2,var3))
elif choice ==0:
	exit()
else:
	print ("We need Tea")



	
