#while else (after while loop is completed, else will be printed)
i=1
while(i<=7):
	if i==5:
		break#(if 4th and 5th line included, then else statement is not printed )
			#(it will break at 4)
	print(i)
	i+=1
else:
	print("Loop completed")
	
print("|||||||||||||||||||")

for i in range(0,9):
	#if i==5:
		#break(if 4th and 5th line included, then else statement is not printed )
			#(it will break at 4)
	print(i)
else:
	print("Loop completed")