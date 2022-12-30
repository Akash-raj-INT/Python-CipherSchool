def outer_func(msg):
    def inner_func():
        print(f"you are kamlesh kemlaesh kalemsh {msg}")
    return inner_func
var=outer_func("jhjhjh")
print(var())