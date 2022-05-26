#getattr, setattr, hasattr,delattr

class student():
	name="ram"
	age=23

#attribute method
print(getattr(student,"name"))# get value 
print(getattr(student,"age"))# get value

setattr(student,"gender","male") #add attribute  to the class
print(getattr(student,"gender"))

setattr(student,"gender","female")# update value
print(getattr(student,"gender"))

print(student.__dict__)# to check all attributes

print(hasattr(student,"name"))#to check attribute exist or not

delattr(student,"gender")
print(student.__dict__)# to check all attributes

#dot notation method
print(student.name)
print(student.age)
print(student.gender)
del student.age
print(student.__dict__)# to check all attributes

