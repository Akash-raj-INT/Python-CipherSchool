a=[1,2,3]
a[0]=100
a[2]=200
print(a)

#Tuples

a=(1,2,3,4)
print(type(a))

def func(*args):
    print(type(args))
func(1,2,3,4)

a=5
b=9
a,b=b,a
c=a,b
print(type(c))

def sum_diff(a,b):
    s = a + b
    d= a - b
    return s,d
s= sum_diff(10,5)
print(s)

a=(1,2,3,4)
print(list(range(5)))
print(tuple(range(5)))

a=[1,2,3,4]
a.append(5)
print(a)
a.append(7)
print(a)

#Dictionaries

a= {
    "name":"Saurabh Sagar",
    1:"something",
    (1,2):"tuple key wat ?"
}

print(a["name"])
print(a[1])
print(a[1,2])

"""
a={
    [1,2]:"something"
}
"""


a={
    "name":"Saurabh Sagar"
}
a["name"]="Bruce"
print(a["name"])



a={
    "name":"Saurabh",
    "company":"Apple Inc",
    "college":"MIT"
}

#print(a["marks"])

key="marks"
if key in a:
    print(a[key])
else:
    print("key doesn't exist")

key="marks"
print(a.get(key))

key="name"
print(a.get(key,"key doesn't exist"))

print(a.values())

for x in a.items():
    print(x)

for key,value in a.items():
    print(key,"->",value)

print(a)

for x in a:
    print(x)

print(list(a))