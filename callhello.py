import hello

print (dir(hello))
print (hello.package)

x = hello.work()
print (x)

object1 = hello.NoWork("pavan","NotWorking")
object1.work_or_nowork()
