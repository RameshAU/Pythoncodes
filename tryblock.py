# to try the code not has error
#if error it shows uniquely 
# otherwise it runs to last

#if doesn't has error
try:#try the code
	a=2/4
	
except Exception as d:# it recognize error and show in output
	print(d)
	
else:#if no error , code will come to this part
	print(a)
	
finally:# if error or no error, this will printed
	print("Thank You")
	
#if has error
try:
	a=2/0
	
except Exception as d:
	print(d)
	
else:
	print(a)
	
finally:
	print("Thank You")

