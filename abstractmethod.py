from abc import ABC,abstractmethod#"abc", "ABC"=abstract base class   

class bank(ABC):# this class should not pass print statement 
	@abstractmethod
	def loan(self): 	pass
	@abstractmethod
	def credit(self): 	pass
	@abstractmethod
	def debit(self): 	pass

class hdfc(bank):#redefine above class and we add more def
	def loan(self):
		print("give loan")
	def credit(self):
		print("give credit")
	def debit(self):
		print("give debit")
	def card(self):
		print("give card")
o=hdfc()
o.loan()
o.credit()
o.debit()
o.card()