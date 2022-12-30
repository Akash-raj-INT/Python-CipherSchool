def finding_num(list1):
    m_list=[str(i) for i in list1 if (type(i)==int or type(i)==float)]
    return m_list
a=["kaluu",1,2,4,1.02,[1,2,3],"kamleshg"]
print(finding_num(a))