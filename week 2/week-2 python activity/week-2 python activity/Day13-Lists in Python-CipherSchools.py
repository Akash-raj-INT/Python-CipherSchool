a=[1,2,3,4]
print(a)

b=["Saurabh",1,1.5,print]
print(b)

a=[1,2,3,4]
a[0]=100
print(a)

print(len([1,3,2,4]))

print("Saurabh" + "Sagar")

print([1,2,3] + [4,5,6])

print([1]*4)

a=[1,2,3,4,5]
for x in a:
    print(x)

print("z" in "Saurabh")

print(1 in [1,2,3,4,5])

a=[1,2,3,4,5]
print(a[-1])

a=[1,2,3]
a.insert(1,100)
print(a)

a=[1,2,3,4]
a.append(5)
print(a)

a=[1,2,3,4]
a.pop()
print(a)

a=[1,2,3,4,5]
a.pop(2)
print(a)

a=["Jatin","Saransh","Jatin","Shubham"]
a.remove("Jatin")
print(a)
a.remove("Jatin")
print(a)

a=[1,3,5,4,6,5]
a.sort()
print(a)

b=[4,1,3,2,6,4]
print(sorted(b))
print(b)

a=[1,2,3,4,5]
a.reverse()
print(a)

b=[1,2,3,4,5]
for x in reversed(b):
    print(x)
print(b)

#Lazy loading vs Eager Loading

#Map function
a=[1,2,3,4]
for i , x in enumerate(a):
    pass

def sqr(x):
    return x**2

for x in map(lambda x:x**2,a):
    print(x)


a=input().split()
print(a)


a=list(map(int,input().split()))
print(type(a[0]))
print(a)

#Join function
print(",".join(["Saurabh","Sagar","Bruce"]))