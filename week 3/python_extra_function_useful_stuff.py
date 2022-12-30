# what is doc string?
# this the strring that we use inside the function to tell other people to what this function doing
# how to use doc string?
# this is data written betweeb '''    ''' or """    """
# how to see doct string?
# print(func_name.__doc__)
# what is help function?

def squares_of_str(str_num):
    ''' this function return square of given number by taking number as a argument'''
    return int(str_num)**2
print(squares_of_str.__doc__)
# we can aso chec pre defined function doc
print(sum.__doc__)

# we can also use help functio0n for that
print(help(sum))
