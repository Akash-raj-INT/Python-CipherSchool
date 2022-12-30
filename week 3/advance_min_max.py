# numbers=[4,5,6,2,3,1,4,5,2,5,8,4,14,1,2,5,8,8,4,1,1,25,5,58,47,1,5,5,5,8,21,14,4]
# print(max(numbers))
names=["satish","kamlesh","navelsh","rajesh","ab","ahshshshshsshhshhsh"]
# how we can calculate which word have the maximum length with max function
# sabse phele normally
def func(item):
    return len(item)

print(max(names,key = func))
# yaha hua kya??? names ke elements ko func mai dal ke nayee kist banaye or uska max nikal ke usko correpondence mai names mai se value de di

dict1={
    "satish kumar":{"math":99,"science":78},
    "kamlesh kumar":{"math":200,"science":100},
    "raju kumar":{"math":45,"science":56},
    "babrao kumar":{"math":56,"science":55},
    "divine kumar":{"math":69,"science":69}
}
print(max(dict1,key=lambda x:dict1[x]["science"]))
print(max(dict1,key=lambda x:dict1[x]["math"]))
print(min(dict1,key=lambda x:dict1[x]["science"]))
print(min(dict1,key=lambda x:dict1[x]["math"]))
