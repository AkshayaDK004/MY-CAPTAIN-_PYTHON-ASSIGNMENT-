n=int(input("enter the range"))
a=0
b=1
c=a+b
print("The fibonacci series is")
print(a)
print(b)
print(c)
for i in range(2,n+1):
	a=b
	b=c
	print(c)
	c=a+b
