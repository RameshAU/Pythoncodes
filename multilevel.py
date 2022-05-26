#multilevel inheritance
class gm:
	def house(self):
		print("gm's house")
class fa(gm):
	def bike(self):
		print("fa's bike")
class son(fa):
	def cycle(self):
		print("son's cycle")
		
o=son()
o.house()
o.bike()
o.cycle()
