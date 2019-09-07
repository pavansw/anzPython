import sys
'''print (sys.argv)'''
if len(sys.argv)==1:
	print ("please give input welcome | bye")
elif sys.argv[1] == "welcome":
	print ("Happy Stay")
elif sys.argv[1] == "bye":
	print ("Bye and Take care")
else:
	print ("Wrong input")
