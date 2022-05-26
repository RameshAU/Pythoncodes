#over write file use key "w"
#append write file use key "a"

#try:
"""
file=open("file.txt", "r")
print(file.read())
"""
"""
#to overwrite file text
file=open("file.txt","w")
file.write("CEG")


file=open("file.txt", "r")
print(file.read())
"""
"""
#to append file text
file=open("file.txt","a")
file.write(" " "CEG chennai")


file=open("file.txt", "r")
print(file.read())
"""
"""
#TO DELETE TEXT FILE
import os

if os.path.exists("text.txt"):
	os.remove("text.txt")
else:
	print("file not found")
	
"""	
"""
#TO DELETE 	folder
import os

if os.path.exists("folder"):
	os.rmdir("folder")
else:
	print("file not found")
"""