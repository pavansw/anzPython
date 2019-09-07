import time
bottels = 100
while bottels in range(101,0,-1):
	print bottels," of the beer on the wall ",bottels,"of the beer \n Take 1 down Go around.."
	bottels-=1
	time.sleep(2)
