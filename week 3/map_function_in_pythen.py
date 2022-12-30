numbers=["2","3","5","8","9"]
def squares_of_str(str_num):
    return int(str_num)**2
# map kewal likha par list ko itrate karke age jo function likha hai like squares_of_str use har element ko dal ke change karke  store kar deta hai but still we have to chnage map into list or tuple otherwise ye kewal map memory location deta hai
squares1=map(squares_of_str,numbers)
squares2=list(map(squares_of_str,numbers))
print(squares1)
print(squares2)
# map is also itrator it will iterate only one time like app es par ek hi bar for loop chala sakte ho