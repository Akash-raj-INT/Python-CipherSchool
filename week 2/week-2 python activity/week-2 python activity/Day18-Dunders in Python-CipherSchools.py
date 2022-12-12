### DUNDERS(magic methods)(event method)
class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello,my name is",self.name)
p=Person("Akash")
p.say_hi()




class A:
    def __init__(self):
        print(self)
        print("initialized")

    def __del__(self):
        print(self)
        print("I am dying")
a=A()


a=1
print(type(a))
print(a+5)

a.__add__(5)

print("akash"*2)
print("akash".__mul__(2))


class A:
    a=1
    b=2
    def __add__(self,x):
        return self.a + self.b + x
a = A()
a + 3
