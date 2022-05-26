import sqlite3

connection=sqlite3.connect('sqlpython.db')

def view():
	query="select * from sqlpython"
	result=connection.execute(query)
	for views in result:
		print(views)
	


print("""
		1.VIEW
		2.INSERT
		3.UPDATE
		4.DELETE
		""")
	
cont=1
while cont==1:
	choice=int(input("Enter Your choice: "))
	if choice==1:
		print("Data in the Database")
		view()
	elif choice==2:
		print("Data to be inserted")
	elif choice==3:
		print("Data to be updated")
	elif choice==4:
		print("Data to be deleted")
	else:
		print("Invalid input and try again")
	cont=int(input("Type 1 to continue: "))
print("Thank you")