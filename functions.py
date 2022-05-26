# types of functions
"""
#no return without argument in python 
def add():
	a=int(input("Enter value of A: "))
	b=int(input("Enter value of B: "))
	c=a+b
	print(c)
add()
"""
"""
#no return with argument in python 
def sub(a,b,c):
	d=a-b-c
	print(d)
	
sub(15,-5,-5)
"""
"""
#return without argument in python 
def mul():
	a=int(input("Enter value of A: "))
	b=int(input("Enter value of B: "))
	c=a*b
	return c
x=mul()
print("total mul: ",x)
"""
"""
#return with argument in python 
def div(a,b,c):
	d=a/b/c
	return d
x=div(15,-5,-5)
print("div: ",x)

"""
"""
#5. arbitary argument function in python
#by using '*' , we can use 'n' number of arguments when calling
def listed (*names):
	print(names)
	
listed("ram","sam","sas","pop")# this program prints in tuple format

def listed (*names):
	print(names)
	for user in names:
		print(user)
listed("ram","sam","sas","pop")# this program prints in one by one by creating loop
"""
"""
#6. keyword argument in python
# based on keyword it allocate value to the particular keys
def data(name,age):
	print(("my name is ",name),("age is: ",age))
	
data(age=25,name="ram")
data(age=21,name="ramesh")
data(age=27,name="prem")
"""
"""
#7. keyword arbitary argument in python
def form(**cv):
	print(cv)
	
form(name="ram", age=23,DOB=1999)
"""
"""
#8. default parameter function in python

def addr(DOB="no dob",name="no name"):# here name defaultly set as "no name", if he doesn't give any value to name argument,it set "no name"
	print(name,", my DOB is",DOB)
	
addr(name="sam",DOB="12-12-2000")
addr(DOB="12-12-2000")
addr()
"""
"""
# 9. passing list as argument in python

def avg(marks):
	return sum(marks)

print(avg([89,90,90,98,99]))

"""
"""
#10. recursive function in python
#calling itself as a value is called recursive function

def factorial(a):
	if a==1:
		return 1
	else:
		return(a*factorial(a-1))
		
print(factorial(10))
"""
#11. lambda function
# it is used to get input directly to the output by using "lambda" keyword
c= lambda total:total+1

print (c(500))

