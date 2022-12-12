#String formatting or String Interpolation
a=5
print("value of a is %d" %(a))
print("value of a is {}".format(a))

a,b,c=1,2,3
print("a={},b={},c={}".format(a,b,c))
print("a={2},b={1},c={0}".format(c,b,a))

name="Saurabh Sagar"
company="Apple Inc"
print("name={name}company={company}" .format(name = name,company=company))
print(f"name={name}")
print("Hello, I am {name} and I work at {company}" .format(name = name,company=company))
print(" Hi {name} welcome to {company}" .format(name = name,company=company))

print(len(r"a\nb"))

for c in r"a\nb":
    print(c)

print("    Saurabh   ".strip())

print("1,2,3,4,5,".split(","))

print("Saurabh Sagar".replace("a","z"))

print("Saurabh Sagar".count("a"))