# it is like map function
numbers=[i for i in range(1,21)]
even__=tuple(filter(lambda x:x%2==0,numbers))
print(even__)
# with map and filter people generally use lamda function rather than defininng one