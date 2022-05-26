#property decorators getter setter
"""
class mark:
	def __init__(self,_total):
		self._total=_total
	@property
	def average (self):
		return self._total/10

sub=mark(490)
print(sub._total)
print(sub.average)
sub._total=500
print(sub._total)
print(sub.average)

print("--------------------")

class mark:
	def __init__(self,_total,name):
		self._total=_total
		self.name=name
	@property
	def average (self):
		return self._total*100/1200
	
	def data(self):
		return self.name
	
print("--------------------")
sub=mark(1190,"raj")
print(sub.name)
print(sub._total)
#print(sub.average) 
print(round(sub.average,2))

print("--------------------")
sub._total=1135
sub.name="Ramesh"
print(sub.name)
print(sub._total)
#print(sub.average)
print(round(sub.average,0))

print("--------------------")
sub._total=1116
sub.name="Ram"
print(sub.name)
print(sub._total)
#print(sub.average)
print(round(sub.average,2))

print("--------------------")
print("--------------------")

# public and private variable
# making private by using "_" 
class student:
	def __init__(self,name,mark,school):
		self.name=name
		self.school=school
		self.mark=mark
	@property
	def data(self):
		return self.name
		return self.school

	
	def mark (self,m):
		if  m<0 or m>500:
			print("invalid mark")
		else:
			self.mark=m
list=student("Ramesh",5000,"SSMHSS")
print(list.name)
print(list.mark)
print(list.school)
list.mark=9999
print(list.mark)
"""

class student:
	def __init__(self,total):
		self._total=total
	@property
	def average (self):
		return self._total/5.0
	
	@property
	def total(self):
		return self._total
	@total.setter
	def total(self,t):
		if t<0 or t>501:
			print("invalid mark")
		else :
			self._total=t
o=student(500)
print(o.total)
print(o.average)
o.total=502
print(o.total)
print(o.average)