keys=input("enter keys: ").split(",")
values=input("enter values: ").split(",")
dect={}
for k in range(0,len(keys)):
    dect[keys[k]]=values[k]
print(dect)
for keys,values in dect.items():
    print(keys,":",values)