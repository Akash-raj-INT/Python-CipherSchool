[4,5,6],[5,6,7],[4,5,9]
avg =lambda *args:[sum(i)/len(i) for i in zip(*args)]
print(avg([4,5,6],[5,6,7],[4,5,9]))