list1=[1,2,3,4,5,6,7,8,9]
list2=[-i if (i%2==0) else i*i for i in list1]
print(list2)