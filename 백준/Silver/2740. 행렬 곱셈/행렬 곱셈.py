import sys
input=sys.stdin.readline

arr1 = []
arr2 = []
N,M= map(int,input().split())
for _ in range(N):
    arr1.append(list(map(int,input().split())))

m,K= map(int,input().split())
for _ in range(m):
    arr2.append(list(map(int,input().split())))

ptr = [[0 for _ in range(K)]for _ in range(N)]

for a in range(N):
    for b in range(K):
        for c in range(M):
            ptr[a][b] += arr1[a][c] * arr2[c][b]

for i in ptr:
    for j in i:
        print(j, end = " ")
    print()