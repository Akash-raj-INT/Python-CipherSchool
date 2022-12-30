from functools import wraps
def only_one_data_type_allow(data_type):
    def decorators(funct):
        wraps(funct)
        def wrapper(*args,**kwargs):
            if all([type(i)==data_type for i in args]):
                return funct(*args,**kwargs)
            else:
                return "invalid argument"
        return wrapper
    return decorators

@only_one_data_type_allow(int)
def sum_of_all(*args):
    temp=0
    for arg in args:
        temp+=arg
    return temp


print(sum_of_all(5,6,4,8,5,85))