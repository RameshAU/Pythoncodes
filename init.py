#  "init" method is used to print userdefined statement when new instance is created
"""
class user:# create new class named "user"
	
	def __init__(self):# this syntax iniatialize the printing when new instance is created
		print("new instance is created")
	
user1= user()#new instance
"""
class user:# create new class named "user"
	
	def __init__(self,name):# this syntax iniatialize the printing when new instance is created
		print("new instance is created")
		self.name=name#  creating  one attribute  "name"
	
	def printall(self):
		print(self.name)#calling "name" attribute to print here
		
user1= user("Ramesh")#new instance
user1.printall()# calling to execute line 16