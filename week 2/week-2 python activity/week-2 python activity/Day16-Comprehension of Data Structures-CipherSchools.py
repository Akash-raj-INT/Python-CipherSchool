#Comprehension

a=[]
for i in range(5):
    a.append(i)
print(a)

a=list(map(lambda x: x**2,range(5)))
print(a)

a=[]
for i in range(5):
    a.append(i**2)
print(a)

#List comprehension
a=[i for i in range(5)]
print(a)

a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)

a=[ [j for j in range(5)] for i in range(5)]
print(a)

n=5
a=[ [ max(i+1,j+1,n-i,n-j) for j in range(n) ] for i in range(n) ]
print(a)

a=[]
for i in range(2):
    for j in range(2):
        a.append(j)
print(a)

a=[j for i in range(2) for j in range(2)]
print(a)

a=[[(i,j) for j in range(2)]for i in range(2)]
print(a)

#Dict Comprehension
a={
    2:4,
    3:9,
    4:16,
}
print(a)

a={ i:i**2 for i in range(5)}
print(a)

#Set Comprehension
a={ i for i in range(5)}
print(a)
print(type(a))

a=(i for i in range(5))
it=iter(a)
print(next(it))
print(type(a))

for x in a:
    print(x)