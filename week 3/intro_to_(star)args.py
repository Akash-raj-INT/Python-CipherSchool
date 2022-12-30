# using * hame jitne bhi args argument dalenge ge function mai wo as a tuple chale jayenge
# like : 
def sumof_all(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sumof_all(1,2,3,4,5,6,85))
# hume abb argument error nahi dega
# *args sare argument ko as a tuple lega
