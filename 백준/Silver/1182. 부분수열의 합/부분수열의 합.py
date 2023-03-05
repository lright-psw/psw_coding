import sys
input=sys.stdin.readline

N,S = map(int,input().split())
ptr = list(map(int,input().split()))
cnt = 0
arr = []
def hap(n):
    global cnt
    if sum(arr) == S and len(arr)>0:
        cnt+=1
    for i in range(n,N):
        arr.append(ptr[i])
        hap(i+1)
        arr.pop()

hap(0)
print(cnt)