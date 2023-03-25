Task 1
radius= float(input("enter the radius : "))
area=22/7*radius*radius
print("The area of circle is",area)

Task 2
filename=input()
if '.py' in filename:
	print("The extension is python")
elif '.c' in filename:
	print("The extension is c")
elif '.cpp' in filename:
	print("The extension is c++")
elif '.java' in filename:
	print("The extension is java")
elif '.js' in filename:
	print("The extension is javascript")
else:
	print("no information")
