class student:
	def __init__(self,total):
		self._total=total
	@property
	def average (self):
		return self._total/5.0
	
	
	def getter(self):
		return self._total
		
	
	def setter(self,t):
		if t<0 or t>501:
			print("invalid mark")
		else :
			self._total=t
	total=property(getter,setter)
			
o=student(500)
print(o.total)
print(o.average)
o.total=350
print(o.total)
print(o.average)