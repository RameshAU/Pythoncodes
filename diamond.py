#diamond problem
class a:
	def display(self):
		print("display a")
class b(a):
	pass
	#def display(self):
	#	print("display b")
class c(a):
	pass
	#def display(self):
	#	print("display c")
class d(b,c):
	pass
	#def display(self):
		#print("display d")

diamond=d()
diamond.display()