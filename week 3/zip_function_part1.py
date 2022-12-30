# it will give a iterator
user_id=[1254,2541,45214]
user_name=["satsi141017","kamlesh","raju","kajuu"]
temp=["ese","swdsd"]
print(zip(user_id,user_name))
print(list(zip(user_id,user_name)))
print(list(zip(user_id,user_name,temp)))


# zip jo ander iterable 2 ya more than 2 lists ya tuple dee jate hai wo on dono mai ek ek dono list mai se elemnt leke  tuples create karta hai bad mai aapp unhe kahi bhi store kra lo

# we can convert [("a",2),("b",5)] these tupe of list to directly to dictionary
list1=[("a",2),("b",5)]
print(dict(list1))

print(dict(zip(user_id,user_name)))
