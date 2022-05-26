class dataw:
	def __init__(self,car):
		self.car=car
	
	def carlist(self):
		for cars in self.car:
			print(cars)
		
	def rem_carname(self,rem_carname):
		self.car.remove(rem_carname)
		print("Car removed")
	
	def add_carname(self,add_carname):
		self.car.append(add_carname)
		print("car added")
		
car=["innova", "Swift", "BMW", "Audi"]
i=dataw(car)

msg= """
		1. view car list
		2. Remove car name
		3. add car name
"""
while True:
	print(msg)
	choice=int(input("Enter your choice"))
	if choice==1:
		i.carlist()
	elif choice==2:
		cars=input("Enter car name")
		i.rem_carname(cars)
	elif choice==3:
		cars=input("Enter car name")
		i.add_carname(cars)
	else:
		print("Invalid input")
		print("Try again")
		quit()