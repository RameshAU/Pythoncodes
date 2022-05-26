#single inheritance is defined as the inheritance in which a derived class is inherited from the only one base class

class indica:#1 base class
	companyname="TATA INDICA"
	year		=1998
	address		="Mount road, Chennai"
	
class i10(indica):#1 derived class
	def __init__(self):
		self.name="TATA INDICA I10"
		self.date=2000
	def details(self):
		print(self.companyname)
		print(self.year)
		print(self.address)
		print(self.name)
		print(self.date)
		
car=i10()
car.details()
