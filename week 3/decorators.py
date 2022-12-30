# Decoraors=== inhance functanility of function
def decorator_function(anu_func):
    def wrapped_func():
        anu_func()
        print("why are u here????")
    return wrapped_func


# now, how to add more functionality to this function
# now this wrapped_func have both hallo world and ectra his own funcyinality
# halloworld=decorator_function(halloworld) 
# halloworld()
# now short cut of using decorator function is using @
@decorator_function #shortcut [its caled sytactic sugar @]
def halloworld():
    print("Hello world ")
# now @ will update halloworld function
halloworld()