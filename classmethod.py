class student:
	name="Ram"
	age=25
	
	def printall():
		print(student.name)
		print(student.age)
		
student.printall()
student.name="som"
print(getattr(student,"name"))