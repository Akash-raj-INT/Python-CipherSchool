"""
student1= {
    "name":"Saurabh Sagar"
    "marks":50
}

student2= {
    "name":"Bruce"
    "marks" : 100
}

"""

class Person:
    pass

p=Person()
print(p)

print(hex(id(p)))

"""
a=1
def square(a):
    print(a**2)
with a:
    square()

"""

class Person:
    name="Saurabh"
    def say_hi(self):
        print(f"Hello Everyone! I am {self.name}")
p=Person()
p.say_hi()  # method call
Person.say_hi(p)   # function call