a=[13,"b",3,True,7.6,"b",34]
print(a)
print(type(a))
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
print(type(a[4]))
print(type(a[5]))
print(type(a[6]))

print("-----------------")

b=[1,3,5,7,8,9]
print("index forward")
print(b)
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])

print("index reverse")
print(b)
print(b[-1])
print(b[-2])
print(b[-3])
print(b[-4])
print(b[-5])
print(b[-6])

print("-----------------")

c=[1,2,5,8,5]
print(c)# before clear
c.clear()
print(c)# after clear
c=[1,2,5,8,5]
d=c.copy()
print(d) #after copying c in d variable
d.pop(2)# remove element based on indexnumber
print(d)
d.remove(8)# remove element based on value( removes appearence of value)
print(d)

print("--------------")

e=[1,2,45,6,2,4]
print(e.count(2))# no of '2' in the list
print(e.index(6))# to find the index of '6'
print(len(e))# to find the no of elements in list
print(max(e))
print(min(e))

print("--------------")

name=["Ram"]
print(name)
name.append("sid")# adding "sid" to the "name" list
print(name)
name.append("rock")# adding "rock" to the "name" list
print(name)
name.append("vas")# adding "vas" to the "name" list
print(name)
name.append("tam")# adding "tam" to the "name" list
print(name)

name1=["sar","kum"]
name.extend(name1)# extending "name1" list to "name" list at end
print(name)

name.insert(1,"ramesh")# inserting "ramesh" word in the index no 1 to "name" list
print(name)

print("----------------------")

print(list(range(4)))# to print value from 0 to less than 4
print(list("Ramesh"))# its split each letter to each value and index no

print("----------------------")

f=[1,9,6,90,2]
g=["orange","cate","dod"]
print(f)
print(g)
f.sort()# to sort the elements in ascending order
g.sort()
print(f)
print(g)
f.sort(reverse=True)# to sort elements in decending order
g.sort(reverse=True)
print(f)
print(g)
g.sort(key=len)# sorthing based on length
print(g)



print("----------------------")