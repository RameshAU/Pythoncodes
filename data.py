#input statement

name = input("Enter your name: ")
print("My name is ",name) 
age= int(input("Enter your age: ") )
print("My age is ",age) 
gender= input("Enter your gender: ")
print("My gender is ",gender)
print( type(name))
print( type(age))
print( type(name))

#input satatement
name1, name2, name3= input("Enter 3 names:")
print ("name1: ", name1)
print ("name2: ", name2)
print ("name3: ", name3)

a="""
Electrical discharge alloying (EDA) is an effective means of adding metal 
powders in the dielectric fluid, and thus by improving the surface chemical and 
mechanical properties of structure materials. The energy from the electrical arc 
can melt the surfaces of the electrode and the work piece, and can decompose the 
powder in the dielectric medium and forms a protective coating. The EDA 
modified layer, which is obtained relatively rapidly, possesses sufficient 
engineering thickness and hardness. The thickness and hardness of this modified 
layer can be controlled by EDA parameters
"""


print(type(a))
print(a)

a= ["12", "34"]
print ("A is: ",a[1])
print ("B is: ",a[0])
print ("c is: ", a[1]+a[0])
print('?'.join(a))

#input statement
Text=[] # it is empty set
print("Enter your lines: ")

while True: #it doesn't complete the until enter is double pressed
	Line= input()# getting input to the "Line"
	if Line:# this check the Line has any lines
		Text.append(Line)# it insert line into the "Text" key
	else:
		break
	print(Text)
out='\n'.join(Text)# it get input to the "out" and print in new line 
print (out)

a=int (input("a: "))
b=int (input("b: "))
c=a+b 
print ("c is : ",float(c))
d= c
print ("d is : ",int(c))
