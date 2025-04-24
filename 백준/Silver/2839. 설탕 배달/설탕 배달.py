INF = 1e9

N = int(input().strip())

DP = [INF] * (N+1)
DP[0] = 0

for i in range(3,N+1):
    if i >=3:
        DP[i] =min(DP[i], DP[i-3] + 1)
    if i>=5:
        DP[i] = min(DP[i], DP[i-5] + 1)

print(DP[N] if DP[N] != INF else -1)