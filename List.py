list=[]
n=int(input("enter the number of elements to be verified"))
print("enter" ,n ,"elements")
for i in range(n):
	x=int(input())
	list.append(x)
print("The list is : ",list)
for i in list:
	if i<0:
		list.remove(i)
print("The new list is : ",list)
