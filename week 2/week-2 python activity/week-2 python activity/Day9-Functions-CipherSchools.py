def show_loading():
    for i in range(3):
        print("loading","."*(i+1))


a=5
b=7
print(a+b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()


def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock",name)
name=sheldon_knock("leonard")

def sheldon_knock(name,times=3):
    for _ in range(times):
        print("knock knock knock",name)

def add(a,b):
    return a+b
a=add(1,2)
print(a)

