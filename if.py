#if else statement
"""
name = input("Enter your name: ")
age= int(input("Enter your age: "))

if age>=18:
	print(name,"Age is ",age,"Eligible for voting")
else :
	print(name,"Age is ",age,"Not Eligible for voting")
"""

#elseif statement
"""
condition
days 0			no fine
	 1-5		1/days
	 6-10		5/days
	 11-30		10/days
	 above 30	membership cancelled


days= int(input("Enter no of days delayed: "))

if days==0:
	print("No fine amount")
elif days>=1 and days<=5:
	print("fine amount is :Rs.",days*1)
elif days>=6 and days<=10:
	print("fine amount is :Rs.",days*5)
elif days>=11 and days<=30:
	print("fine amount is :Rs.",days*10)
else:
	print("Membership cancelled")
"""

#nested if statement
"""
mark1=int(input("Enter 1st mark: "))
mark2=int(input("Enter 2nd mark: "))
mark3=int(input("Enter 3rd mark: "))

Total=mark1+mark2+mark3
print("your total mark is: ",Total)

Avg= Total/3
print("your Average mark is: ",Avg)

if Avg>=70 and Avg<=100:
	if Avg>=90 and Avg<=100:
		print("You get A grade")
	elif Avg>=80 and Avg<90:
		print("You get b grade")
	elif Avg>=70 and Avg<80:
		print("You get c grade")
	else:
		print("You get D grade")
elif Avg<70:
	print("You are fail")
else:
	print("Invalid mark")
"""


