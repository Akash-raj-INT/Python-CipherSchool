from functools import wraps
import time
def calculate_time_of_func(anyf):
    
    @wraps(anyf)
    def wrappedf(*args,**kwargs):
        t1=time.time()
        return_val= anyf(*args,**kwargs)
        t2=time.time()
        print(t2-t1)
        return return_val
        
    
    
    return wrappedf

@calculate_time_of_func
def square(num1):
    k=[]
    
    for i in range(1,num1+1):
        k.append(i**2)
    return k

print(square(60))