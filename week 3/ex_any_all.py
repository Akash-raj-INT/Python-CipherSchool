def sum_all(*args):
    if all([type(j)==int or type(j)==float for j in args]):
        temp=0
        for i in args:
            temp+=i
        return temp
    else:
        return "Enter a valid response"
print(sum_all(4,5,6,8,5,4,7,5.25))