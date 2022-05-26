"""
class user:

	def __init__(self,carname,modelno):
		self.carname=carname
		self.modelno=modelno
		self.profile= self.carname+self.modelno	#concatenate both carname and modelno

instance=user("innova","546546")#concatenate  possible only in string so any type should be use string type
print(instance.carname)
print(instance.modelno)
print(instance.profile)
# if you need to update any values
instance.modelno= 446441# after execution, value is not  changed , so follow step 3 program
print(instance.profile)


#step 3
class user:
	
	def __init__(self,carname,modelno):
		self.carname=carname
		self.modelno=modelno
		
	def profile(self):
		return self.carname+str(self.modelno)

#slove the update eror in 1st program use line 24,25 
#it makes the "profile" separate function 

instance=user("innova",546546)#concatenate  possible only in string so any type should be use string type
print(instance.carname)
print(instance.modelno)
print(instance.profile())# to call the function use "()" at end or else use step 4 program  

instance.modelno= 446441#updating new value
print(instance.profile())

instance.carname= "tata"
print(instance.profile())
"""

#step 4
class user:	
	def __init__(self,carname,modelno):
		self.carname=carname
		self.modelno=modelno
		
	@property	#by using this , no"()" needed while calling the function
	def profile(self):
		return self.carname+str(self.modelno)

instance=user("innova",546546)
print(instance.carname)
print(instance.modelno)
print(instance.profile)  

instance.modelno= 446441#updating new value
print(instance.profile)

instance.carname= "tata"
print(instance.profile)
