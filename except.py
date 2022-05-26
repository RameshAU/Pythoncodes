#exceptions in python

"""
#zerodivisionerror
try:
	a=10/0
	
except ZeroDivisionError in a:
	print ("den can't be zero")

print("------------------------")
"""
"""
#FileNotFoundError 
try:
	f = open("text.txt")
	
except FileNotFoundError in f:
	print ("file not found")

else:
	print(f.read())
	
print("------------------------")

#IndexError
try:
	i= [12,34,6,76,5]
	print(i[9])
except IndexError in i:
	print("invalid index no")
else:
	print(i[2]+5)
"""
"""
#ValueError 
try:
	a=float("joes")
	print(a)
except ValueError in a:
	print("Please enter no")
else:
	print(a)
"""