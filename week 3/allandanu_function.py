number1=[1,2,3,4,5,6,7,8,9]
numbers2=[2,4,6,8,10,12,14,16,18]
print(all([i%2==0 for i in number1]))
print(all([k%2==0 for k in numbers2]))
print(any([j%2==0 for j in number1]))
print(any([l%2==0 for l in numbers2]))