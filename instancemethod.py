class student:
	name="Ram"
	age=25
	
	def printall(self,clg):
		print(student.name)
		print(student.age)
		print(clg)
a= student()
"""
a.printall()
"""

student.printall(a,"B.E")