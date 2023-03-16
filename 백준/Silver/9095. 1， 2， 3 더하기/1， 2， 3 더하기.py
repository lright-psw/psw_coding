import sys
input = sys.stdin.readline

N = int(input().rstrip())
DP = [0] * 11
DP[1] = 1
DP[2] = 2
DP[3] = 4
for _ in range(N):
    n = int(input().rstrip())
    for i in range(4, n+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    print(DP[n])
