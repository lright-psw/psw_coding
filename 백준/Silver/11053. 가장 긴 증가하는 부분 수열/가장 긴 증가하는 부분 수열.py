import sys
input=sys.stdin.readline

N = int(input().rstrip())
DP = [1] * N
seq = list(map(int,input().split()))
for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            DP[i] = max(DP[i],DP[j]+1)
print(max(DP))