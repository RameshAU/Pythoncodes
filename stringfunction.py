# note: Python is Case sensitive
"""
a="python is program"

print(a)# to print a
print(type(a))#to print type of a
print(a.upper())# to make uppercase a
print(a.lower())# to make lowercase a
print(a.capitalize())#to make uppercase to first letter of the line
print(a.title())#to make uppercase to first letter of each word in line
print(a.count("python"))# to count no of words
print(a.count("p"))# to count no of "p" characters
print(a.endswith("am"))# to check the line ends with "am"
print(a.startswith("py"))# to check the line starts with "py"
print(a.find('i'))# to find the index no of any letters like'i' or 'p'
print(a.replace("is","was"))# to find and replace the word( eg: to find "is"and to replace with "was")
print("a is upper:", a.isupper())# to check the words are in uppercase and give boolean answer
print("a is lower:", a.islower())# to check the words are in lowercase and give boolean answer
print("a has only alphabet: ",a.isalpha())# to check line has only alphabet
print("a has  alphabet and numbers: ",a.isalnum())# to check has both no and letters
b="python\n,is\n,program"
print(b)# to print b
print(b.splitlines())# to print the line by each word separated by ',' # it only consider the word
b=("he" "is" "boy")
print(b.splitlines(True))# to print the line by each word separated by ',' # it includes letter and symbols word
"""
c="      python   "
print(len(c))# count the no of characters and symbols( space also)
print(len(c.strip()))# count the no of lettrs in the word only
print(len(c.lstrip()))# count the no of lettrs in the word and space except left side spaces
print(len(c.rstrip()))# count the no of lettrs in the word and space except right side spaces

d="12-01-2022"
print(d.partition('-'))# to create partition to the date and split as (dd, -, mm-yyy)

#string manipulation
A= "abcdef"
"""
index value
a=0,  b=1,  c=2,  d=3,  e=4,  f=5
a=-6, b=-5, c=-4, d=-3, e=-2, f=-1
"""

print(A)# to print the A value
print(A[0])# to print the letter which has index value 0
print(A[-2])#to print the letter which has index value -2022
print(A[:2])# to print letters upto index no 2 from first
print(A[:-2])# to print letters except last two letters from first 
print(A[::-1])# to print letters in the word in reverse order fully [ans: fedcba]
print(A[::-2])# take reverse order"fedcba"  then print first letter and print 3rd 5th letter [ans:fdb]
print(A[::-3])# take reverse order"fedcba"  then print first letter and print 4th letter[ans:fc]
print(A[::-4])# take reverse order"fedcba"  then print first letter and print 5th letter [ans:fb]
print(A[::-5])# take reverse order"fedcba"  then print first letter and print 6th letter[ans:fa]
print(A[::-6])# take reverse order"fedcba"  then print first letter only[ans:f]
print(A[3:-2])# to print letters start with index no 1 to less than index no -2
