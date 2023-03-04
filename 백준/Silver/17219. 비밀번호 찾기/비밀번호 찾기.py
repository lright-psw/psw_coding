import sys
input=sys.stdin.readline


N,M = map(int,input().split())

dic = {}
ptr = []
for i in range(N):
    site = input().split()
    dic[site[0]] = site[1]
for i in range(M):
    a=input().rstrip()
    ptr.append(dic[a])
    
print(*ptr,sep="\n")
