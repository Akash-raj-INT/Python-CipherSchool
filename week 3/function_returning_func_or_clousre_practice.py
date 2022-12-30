# we also call it clouser and first class function
def power_num(pow):
    def power_of_num(num):
        return num**pow
    return power_of_num
cube=power_num(3)
square=power_num(2)
print(cube(5))
print(square(5))