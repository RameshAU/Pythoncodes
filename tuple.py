print("tuple() is same as list[]")

a=(1,2,3,"r",True)

print(a)
print(type(a))
b=list(a)
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

print("-------------")

print("how python recognize the tuple")

a=(1)# this recognize as integer type
print(type(a))

a=(1,)# this recognize as tuple type
print(type(a))

print("-------------")

print("to conatenate two or more tuple")

a=(1,3,4)
b=(2,4,5,8)
c=(3,67,89)
print(a+b)# it concatenate a and b
print(a+b+c)# it concatenate a, b and c

#we can also concatenate list
a=[1,3,4]
b=[2,4,5,8]
print(a+b)# it concatenate a and b

#to print multiple times
a=(" Ram ")# it takes as string and print continuouslu
print(a*10, end=" ")

a=("Ram",)# it takes as tuple and print as tuple
print(a*5)

