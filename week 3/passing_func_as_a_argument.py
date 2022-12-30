# u know how amp function works lets make aou own map function
# we can assign variable as a function like
def cuberoot(num):
    return(num**(1/3))
def cube(num):
    return(num**3)
def squaref(num):
    return(num**2)
def sqroot(num):
    return(num**(1/2))

def my_map(func,num):
    return func(num)
print(my_map(cuberoot,5))
print(my_map(cube,5))
print(my_map(sqroot,5))
print(my_map(squaref,5))