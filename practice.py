class library:
	def __init__(self,books):
		self.books=books
	
	def list(self):
		for book in self.books:
			print(book)
	
	def bor_book(self,bor_book):
		self.books.remove(bor_book)
		print("book borrowed")
		
		
	def add_book(self,add_book):
		self.books.append(add_book)
		print("book added")
		
		
books=["c","java","python","c++"]
a=library(books)

msg= """
	1.view available books
	2.remove book
	3.add book
"""

while True:
	print(msg)
	choice= int(input("Enter your choice: "))
	
	if choice==1:
		a.list()
	elif choice==2:
		book=input("Enter name of book to remove")
		a.bor_book(book)
	elif choice==3:
		book=input("Enter name of book to add")
		a.add_book(book)
	else:
		print("Invalid input and Try again")
		quit()