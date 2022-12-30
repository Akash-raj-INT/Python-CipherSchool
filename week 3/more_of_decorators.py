# only int allow decorator
from functools import wraps
def only_int_allow(funct):
    wraps(funct)
    def wrapper(*args,**kwargs):
        if all([type(i)==int for i in args]):
            return funct(*args,**kwargs)
        else:
            return "invalid argument"
    return wrapper

@only_int_allow
def sum_of_all(*args):
    temp=0
    for arg in args:
        temp+=arg
    return temp


print(sum_of_all(5,6,4,8,5,85))
