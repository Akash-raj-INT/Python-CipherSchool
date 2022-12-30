def findingcube(n):
    dect1={}
    for i in range(1,n+1):
        dect1[i]=i**3
    return dect1
a=int(input("enter the number : "))
print(findingcube(a))