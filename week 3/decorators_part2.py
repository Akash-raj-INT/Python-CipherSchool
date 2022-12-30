def decorator_function(anu_func):
    def wrapped_func(*args,**kwargs):
        print("why are u here????")
        return anu_func(*args)
    return wrapped_func
# @decorator_function
# def num1(a):
#     print(f"this is function with argument {a}")
# num1(5)
# ok to * args ka use karke argument walee problem solve ho gaye
# but but but but but lets defincr one more func
# lets decorate it
@ decorator_function
def add(c,d):
    return c+d
print(add(5,7)) # on printion it will return none beacaues uper hamne any funvtion mai return nahi likha hai to any function kuch return nahi karega lets solve it
