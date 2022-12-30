def cubes(nums,*args):
    if len(args)>0:
        return [i**nums for i in args]
    else:
        return "enter a valid response"
   
nums=[1,2,3,4,5]
print(cubes(5))
