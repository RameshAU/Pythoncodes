# set is unordered and unindex type
# it is given in curly braces{}
# functions in 'set'= add, update, remove, discord, delete
#duplicate values are removed automatically
#List = []  , tuple= () ,  set = {}
"""
names={"ram","arun","var"}
print(names)
print(type(names))

names.add("sara")#add "sara" in names
print(names)

name1={"arun","karthik"}
names.update(name1)#update name1 values in names
print(names)

names.pop()#it removes the random values
print(names)

names.remove("arun")#it removes given value 
#if it doesn't have it shows error
print(names)

names.discard("varun")#it removes given value 
#if it doesn't have it doesn't shows error
print(names)

names.clear()# it clears set values and show empty set as "set()"
print(names)

del names# it delete the whole 'names' set


print("---------------------------")
"""
#union,intersection,intersection_update 
#symmetric_difference,symmetric_difference_update

a={1,5,7}
b={3,5,9}

"""
c=a.union(b)# it joins both set values and remove duplicate value
print(c)

a.update(c)
print(a)

c=a.intersection(b)
print(c)

a.intersection_update(c)
print(a)

c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(c)
print(a)

"""
# isdisjoint, issubset, issuperset

a={1,3,6}
b={1,3,6}

print(a.isdisjoint(b))# true='if both set has different elements
					  # false='if both set has atleast one same elements
print(a.issubset(b)) # true='if one set has all same elements of another set
#eg:a={1,2,3} b={1,2,3,4,5}  'b' has all elements of 'a'
print(a.issuperset(b))#true='if both set has only same elements
#eg: a={1,3,6} b={1,3,6} "b" has equal and same elements of "a"
