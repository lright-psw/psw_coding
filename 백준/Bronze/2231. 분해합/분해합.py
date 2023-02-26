import sys
input=sys.stdin.readline


N = int(input().rstrip())

for i in range(1,N+1):
    cnt = i
    for j in str(i):
        cnt += int(j)
        
    if cnt == N:
        print(i)
        break
    elif N == i:
        print(0)