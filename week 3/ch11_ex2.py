def func(name,**kwargs):
    if kwargs.get("rev")==True:
        name=[j[::-1] for j in name]
    return [i.title() for i in name]
names=["sarish","hitsh","kallua"]
print(func(names,rev=True))