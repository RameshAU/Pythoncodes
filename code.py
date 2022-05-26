"""
str1= input("ENter text 1: ")
str2=input("ENter text 2: ")

if (sorted(str1)==sorted(str2)):
	print("It is anagrams")
else:
	print("It is not anagrams")
"""
"""
lop=[10,24,5,78]
sum=0
for i in lop:
	sum=sum+i
print(sum)

"""
"""
nterms=int(input("Enter number"))
n1=0
n2=1
count=0

if nterms <= 0:
	print("enter positive number")
elif nterms==1:
	print(n1)
else:
	print("fibonacci series: ")
	while count<nterms:
		print(n1)
		nth=n1+n2
		n1=n2
		n2=nth
		count +=1
"""
"""
num=int(input("Enter number: "))
factorial=1

if num<0:
	print("Factorial is not applicable")
elif  num==0:
	print("Factorial of 0 is 1")
else:
	for i in range(1,num+1):
		factorial=factorial*i
	print(factorial)
"""
"""
word= input("Enter text")
count=0
for i in word:
	if i.lower() in ['a','e','i','o','u']:
		count+=1
print(count)
"""
"""
print(msg)
date=input("Enter date:")

day=date[0:2]
month=date[3:5]
year=date[6:10]

print(day)
print(month)
print(year)
"""
"""
num=int(input("Enter number: "))
str=num
total=0
while str!=0:
	k = str%10
	total+=k*k*k
	str=str//10
if total==num:
	print("It is armstrong number")
else:
	print("It is not an armstrong number")
"""
"""
num=int(input("Enter number: "))
sum_odd=0
sum_even=0

while  num>0:
	rem=num%10
	if rem%2==0:
		sum_even=sum_even+rem
	else:
		sum_odd=sum_odd +rem
	num=num//10

print(sum_even)
print(sum_odd)
"""
num=input("Enter number:  ")

print(num[::-1])
















