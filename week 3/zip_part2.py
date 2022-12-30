# * in zip functions

list1=[(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*list1)))
# * list1 mai jo andar tuples hai unko todd kar 2 alag alag tuple de dega 
# like [(1, 3, 5, 7), (2, 4, 6, 8)]
list2,list3=list(zip(*list1))
print(list(list2))
print(list(list3))