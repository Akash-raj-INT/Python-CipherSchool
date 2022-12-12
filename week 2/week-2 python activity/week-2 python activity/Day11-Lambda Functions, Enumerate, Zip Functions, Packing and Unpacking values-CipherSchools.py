#Lambda Expressions
c=lambda a,b: a+b
print(c)
print("Hello World")
show=print
show("something")

names=["Jatin","Saransh","Samarth"]
for name in names:
    print(name)


names=["Jatin","Saransh","Samarth","Shubham"]
for name in enumerate(names):
    print(name)


a={1,2,3}
names=["Jatin","Saransh","Samarth","Shubham"]
for a in enumerate(names):
    print(a[0],a[1])

#Packing and Unpacking Values
#1
a=5
b=9

a=a+b
b=a-b
a=a-b
print(a,b)

#2
a=5
b=9

a=a^b
b=a^b
a=a^b
print(a,b)

#3
a=5
b=9
temp=a
a = b
b=temp
print(a,b)


a=[1,2]
b,c=a
print(b,c)


a= 1 , 2
print(type(a))

a=5 ;b=9
a , b = b ,a
print(a,b)


names=["Jatin","Saransh","Samarth","Shubham"]
for i, name in enumerate(names):
    print(i,"-",name)


names=["Jatin","Saransh","Samarth","Shubham"]
scores=[50,80,90,70]
for a  in zip(names,scores):
    print(a)

names=["Jatin","Saransh","Samarth","Shubham"]
scores=[50,80,90,70]
cities=["delhi","patna","kolkata","mumbai"]
for name,score,city  in zip(names,scores,cities):
    print(name,"-",score,"-","city")