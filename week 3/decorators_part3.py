from functools import wraps

def decorator_function(anu_func):
    @wraps(anu_func)
    def wrapped_func(*args,**kwargs):
        """this is wrapped function"""
        print("why are u here????")
        return anu_func(*args)
    return wrapped_func
@ decorator_function
def add(c,d):
    """This is add function"""
    return c+d
# now think after decorating the function kya decorator function decorator reh gya hai
# lets see string docs to yadd hi hoga jo """   """ ke bech mai likha jata hai
print(add.__doc__)#jaise dekh sakte hai add function abb add function nahi reh gya
print(add.__name__)
# how to solve this problem
# hum imprt karege from functiontools import wraps