class ase:#base class
	def workhours(self):
		self.hours=45
	def printing(self):
		print("Working hours: ",self.hours)
	
class trainee(ase):#derived class
	def workhours(self):
		self.hours=75
		
	def resethrs(self):#reseting derived value to base class
		super().workhours()#super()- keyword to reset

o=ase()#access base
o.workhours()
o.printing()

print("-------------------")

t=trainee()#access base class via derived class
t.workhours()
t.printing()

print("-------------------")

t.resethrs()#calling reset function
t.printing()