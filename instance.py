class user:# main class
	name="ram"
	course="python"
	
user1=user()#instance
print(user1.__dict__)
print(user1.name)#these three lines check "user1" has any "name" attributes otherwise goes main class "user"

user1.name="som"   #adding "name" attributes to user1(instance)
print(user1.__dict__)
print(user1.name)#these three lines check "user1" has any "name" attributes otherwise goes main class "user"


