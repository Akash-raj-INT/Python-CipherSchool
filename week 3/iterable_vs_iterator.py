# iter funcyion
# jab hum kisi list tuple ya string par lop chalate hai to wo unhe first ek ierrator mai chnage karta hai using iter function
numbers=["2","3","5","8","9"]
# step 1 for loop change numbers into itrator object
num1=iter(numbers)
print(num1)
# uske bas uske next next  value deta jata hai jaise
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))

# like u can see hum bina list ko iter mai convert kiye next function ko nahi use kar sakte

# where map is already aa iterator use iterator mai convert karne ki koi jaroort nahi hotee
squares=map(lambda x:int(x)**2,numbers)
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))