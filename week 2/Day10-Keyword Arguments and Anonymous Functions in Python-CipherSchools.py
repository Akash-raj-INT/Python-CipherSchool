def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(c=1,a=2,b=3)

def hello():
    print("Hello World !")
a=1
a=hello
a()

hello=2
print(hello)

a()

def hello():
    return 1
print(hello)
print(hello())

# args  kwargs

#Required arguments
def func(a,b):
    print(a,b)
func(1,2)

# Default arguments
def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(3,4)

#Optional positional only arguments
def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,4)

def  func(*c):
    print(c)
func()

#Required Keyworded only arguments
def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,5,6,7,d=8)


#Default keyworded only arguments
def func(a,b,*c,d,e="akash"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,3,4,d="something",e="asdf")

#Optional keyworded only arguments
def func(**k):
    print(k)
func(name="akash")


#Anonymous function or Lambda Functions

a=lambda a,b: a + b
print(a)
print(a(1,2))

def func(a):
    a()
def asdf():
    print("akash")
func(a=lambda:print("hello"))







