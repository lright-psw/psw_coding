import sys
input = sys.stdin.readline

arr = []
n, m = map(int,input().split())
for i in range(1,n+1):
    arr.append(i)
for i in range(m):
    a,b = map(int,input().split())
    tmp = arr[b-1]
    arr[b-1] = arr[a-1]
    arr[a-1] = tmp

print(*arr,sep=' ')