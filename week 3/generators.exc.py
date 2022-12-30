def only_eve(num):
    for i in range(1,num+1):
        if i%2==0:
            yield i
for i in only_eve(21):
    print(i)
for j in only_eve(21):
    print(j)
# ye chalega kyuki hum 2 bar generatae create kar rahe hain