# 
class student:
	count= 0
	def __init__(self,name,age):
		self.name=name
		self.age=age
		student.count+=1
		
	def details(self):
		#print("name: ",self.name,"age: ",self.age)
		return ("name: ",self.name +" "+ "Age: ",self.age)
		
	@classmethod
	def total(clas):
		return clas.count

o=student("Ramesh","45")
print(o.details())

o=student("Aravind","76")
print(o.details())

print("Total Admission: ",o.total())
print("Total Admission: ",student.total())