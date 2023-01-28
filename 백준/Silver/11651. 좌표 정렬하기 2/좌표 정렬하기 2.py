import sys

n = int(input())
ptr=[]
for i in range(n):
    [x,y]=map(int,input().split())
    ptr.append([y,x])
    

ptr.sort(reverse=False)

for i in range(n):
    print(ptr[i][1], ptr[i][0]) 