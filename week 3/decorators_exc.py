from functools import wraps
def print_function_data(any_func):
    wraps(any_func)
    def wrapped(*args,**kwargs):
        print(f"ypur function name is {any_func.__name__}")
        print(any_func.__doc__)
        return any_func(*args,**kwargs)
    return wrapped
@print_function_data
def add_num(a,b):
    """ this is add fynction """
    return a+b
print(add_num(6,7))


