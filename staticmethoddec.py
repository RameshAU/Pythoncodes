#static method
class student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	def details(self):
		print("Name: ",self.name,"Age: ",self.age)
	
	@staticmethod
	def welcome():
		print("Welcome to all")

o=student("Ramesh",35)
o.details()
o.welcome()

o2=student("Ram",25)
o2.details()
o2.welcome()