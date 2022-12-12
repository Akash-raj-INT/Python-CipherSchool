#Sets

a={1,2,3,4,5}
print(type(a))

for i in a:
    print(i)

a={1,2,3,4}
b={3,4,5,6}
print(a - b)

print(a.union(b))

print(a.intersection(b))

a.add(1)
print(a)

a.remove(4)
print(a)

a=[[ "" ]*3]*3
a[1][1]="x"
print(a)

print(id(a[0][1]))
print(id(a[1][1]))
print(id(a[2][1]))

a=[1,2,3,4,5]
print(id(a[1]))

a[0]=100
a=1
print(id(a))

a=2
print(id(a))

"""
class Student:
    name="Saurabh"
    marks=50

"""

a,b=258,258
print(a==b)
print(a is b)

a=(1,2,3)
print(hash(a))

a="Saurabh"
print(hash(a))