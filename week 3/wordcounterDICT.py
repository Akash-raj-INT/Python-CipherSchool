def word_counter(str1):
    dect={}
    for i in str1:
        dect[i]=str1.count(i)
    return dect
a=input("Enter a string : ")
print(word_counter(a))