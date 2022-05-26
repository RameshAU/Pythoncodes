#data abstraction oly provide essential info to outside and hide background details
#data encapsulation is a wrapping code and data together into single unit

class fourthyear:#creating class
	def __init__(self,name):	#iniatialize varaiable"name"
		self.name=name #add name to self.name
		
	def listnames(self):# creating list function
		print("name list of the 4th year: ")
		for names in self.name:
			print(names)
		
	def removename(self,removename): #remove name function
		print(removename,"Name removed")
		self.name.remove(removename)# remove input name
		
	def addname(self,addname): #add name function
		print(addname,"Name added ")
		self.name.append(addname)#add input name

name=["aravinth","dinesh","guna", "sid","mithun"]# creating names
o=fourthyear(name)#insert "name" list in class "fourthyear"
#message to be displayed
msg= """
		1. view namelist
		2. remove name
		3. add name
		"""
 		
while True:#if above has no error , print msg
	print(msg)
	choice=int(input("Enter your choice: "))#getting choice
	if choice==1:
		o.listnames()#execute listname function
	elif choice==2:
		names=input("Enter name to remove: ")
		o.removename(names)#execute removename function
	elif choice==3:
		names=input("Enter names to add: ")
		o.addname(names)#execute addname function
	else:
		print("Invalid input try again")
		quit()# if invalid input , quit the program