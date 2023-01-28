import sys

n=input()
arr=[]
for i in str(n):
    arr.append(i)

arr.sort(reverse=True)

print(''.join(arr))