"""
file=open("file.txt", "r")
#print(file.read())-read the full file
#print(file.readlines())- read the fulltext in list form
#print(file.readline())- this only print the one line
# use mutiple "readlin" cmd to print reamaining line



try:
	file=open("file.txt","r")
	print(file.read())
	
except FileNotFoundError :
	print("File not found")

else:
	file.close()

"""
"""#print the lines in the file one by one
try:
	file=open("fil.txt","r")
	for l in file:
		print(l)
	
except FileNotFoundError :
	print("File not found")

else:
	file.close()
"""
