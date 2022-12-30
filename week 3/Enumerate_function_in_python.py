names=["kamlesh","raja","kalua","kakakkkaka"]
def findpos(find1,list1):
    k=0
    for position,name in enumerate(list1):
        if name==find1:
            return position
            k+=1
    return -1
        
print(findpos("raja",names))
    