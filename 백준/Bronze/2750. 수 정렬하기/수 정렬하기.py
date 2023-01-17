n=int(input())
ptr=[]

for i in range(n):
    ptr.append(int(input()))
ptr.sort()

for i in range(len(ptr)):
    print(ptr[i])
