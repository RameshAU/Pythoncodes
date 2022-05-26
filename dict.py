#dictionary(dict)

user= {"name":"abc","age":"25"}

print(user)#it prints fully
print(user.keys())#it only prints keys
print(user.values())#it only prints values
print(user.items())#it both prints keys and values

for x in user:# to input "user" value in x and print x
	print(x)

for x in user:# to input "user" value in x and print x
	print(x,"",user[x])

for x in user.keys():# to input "user keys" value in x and print x
	print(x)

for x in user.values():# to input "user values" value in x and print x
	print(x)

for x in user.items():# to input "user keys and values" value in x and print as individually in ()
	print(x)
	
if "named" in user:
	print("yes")
else:
	print("no")

#to update in user 
user.update({"gender":"male"})
print(user)	

#to change in user 
user["gender"]="female"
print(user)	

# to remove(pop) element
user.pop("age")
print(user)

#to clear element
user.clear()
print(user)

#we can also use nested dict

users={
		"user1":{"name":"abc","age":"25"},
		"user2":{"name":"abcd","age":"35"}
}
print(users)