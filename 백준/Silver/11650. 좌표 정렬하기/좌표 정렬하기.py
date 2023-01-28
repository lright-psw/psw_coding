import sys

n = int(input())
ptr=[]
for i in range(n):
    [x,y]=map(int,input().split())
    ptr.append([x,y])
    

ptr.sort(reverse=False)

for i in range(n):
    print(ptr[i][0], ptr[i][1])