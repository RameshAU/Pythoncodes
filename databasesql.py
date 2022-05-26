import sqlite3

connection= sqlite3.connect('Ramesh.db')

def insertdata(name,age,city):
	query="insert into Ramesh(NAME,AGE,CITY) values (?,?,?);"
	connection.execute(query,(name,age,city))
	connection.commit()
	

print("""
		1. insert
		2. Update
		3. Delete
		4. Select
		""")
	
ch=1
while ch==1:
	c=int(input("Enter your choice: "))
	if c==1:
		print("Add the data")
		name=input("Enter your name")
		age=int(input("Enter your age"))
		city=input("Enter your place")
		insertdata(name,age,city)
		
	elif c==2:
		print("update the data")
	elif c==3:
		print("delete the data")
	elif c==4:
		print("view all data")
	else:
		print("Invalid input")
	ch=int(input("Enter 1 to continue: "))
print("Thank You")