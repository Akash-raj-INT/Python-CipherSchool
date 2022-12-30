# create a genrator wth generatoe function
# 1. using generators function
def gen1(num):
    for i in range(1,num+1):
        yield i
# if we use yeild keyword it will srore gen1 as a genrator [its imp keyword]
numbers=gen1
print(numbers)
# scence numbers is a genraotr it will print only one time
for i in numbers:
    print(i)
for j in numbers:
    print(j)
