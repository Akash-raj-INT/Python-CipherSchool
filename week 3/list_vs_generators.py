# list vs genrators
# meomry and time
# when to use list and when tu use generators
import time
t1=time.time()
# l1=[i for i in range(100000000)]
gen1=(i for i in range(100000000))

t2=time.time()
print(t2-t1)
# as u can see list and genrators create hone mai kitna time lagta hai generators are very fast as compare to list
# you can also check memory usage by opening and watching you task manager


# we use list when we have to store our data and lagatar we have tu use functains on it
# on the other hand