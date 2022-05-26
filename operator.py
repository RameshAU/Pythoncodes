"""
#Arithmetic operators

a=14
b=3
print(a+b)#addition operator
print(a-b)#subraction operator
print(a*b)#multiplication operator
print(a/b)#division operator ( print quotient value including decimal)
print(a%b)#modulus division operator ( print the remainder value)
print(a//b)#floor division operator( print quotient value removing decimal)
print(2**5)# it make exponetial 2^5(32)
"""
"""
#Assignment operators
a=20
print(a)# to print 'a' value
a+=10
print(a)# a=a+10
a-=10
print(a)#a=a-10
a*=10
print(a)#a=a*10
a/=10
print(a)# a=a/10
a%=10
print(a)# a=a%10
a**=10
print(a)# a=a^10
a//=3
print(a)# a=a//3
"""

"""
# relational or comparison operators

a=25
b=50

print(a==b)# a equal to b
print(a!=b)# a not equal to b
print(a<=b)# a less than or equal to b
print(a>=b)# a greater than or equal to b
print(a<b)# a less than b
print(a>b)# a greater than b
"""
"""
#logical operator

and 
or
not

maths= 50 
print(maths>=25 and maths<=51)# in "and" , both conditios to be satisfied to become true
print(maths>= 45 or maths>=52)# in "or" , both conditios to be satisfied to become true
print(not(maths>=25 and maths<=51))# in "not" , reverse of and 
print(not(maths>= 45 or maths>=52))# in "not" , reverse of or
"""

# bitwise operator
"""
& AND
| OR
^ XOR
~ NOT
<< zero fill left shift( make the binary digits to 8)
>> remove last value as per count (if a>>2 and binary is 10101, then remove last two value. ans; binary to decimal of(101)
"""
a=50
b=55
print(a&b)
"""
a=20 b=30
binary of 20= 10100
binary of 30= 11110
a&b         = 10100
decimal of 10100= 20
"""
print(a|b)
"""
a=20 b=30
binary of 20= 10100
binary of 30= 11110
a|b         = 11110
decimal of 11110= 30
"""
print(a^b)
"""
a=20 b=30
binary of 20= 10100
binary of 30= 11110
a|b         = 01010( both 1 or 0 =0 , difference=1)
decimal of 1010= 10
"""
print(~a)
"""
a=20 
~a= add 1 to a and put minus sign
~a= -21
"""
print(a<<4)
"""
a=20
binary of 20 = 10100(taken to 8 bits = 00010100) now shift first 2 bits to last= 1010000
decimal of 1010000= 80
"""
print(a>>3)
"""
a=20
binary of 20 = 10100(taken to 8 bits = 00010100) now shift last 2 bits to first= 0000101=101
decimal of 101= 5
"""
