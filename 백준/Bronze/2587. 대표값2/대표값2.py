ptr=[]

for i in range(5):
    ptr.append(int(input()))
ptr.sort()

avg = int(sum(ptr))/5
mid = ptr[2]

print("{0}\n{1}".format(int(avg),int(mid)))