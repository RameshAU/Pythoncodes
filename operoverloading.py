#we cannot add instance so we use "__add__", "__sub__",etc function
class add:
	def __init__(self,a):
		self.a=a
	def __add__(o1,o2):
		return o1.a + o2.a
	
	def __sub__(o1,o2):
		return o1.a - o2.a
	
	def __mul__(o1,o2):
		return o1.a * o2.a
o1=add(24)
o2=add(24)


print(o1+o2)
print(o1-o2)
print(o1*o2)