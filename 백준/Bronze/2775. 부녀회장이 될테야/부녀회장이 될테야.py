T = int(input().strip())

dp = [[0]* 15 for _ in range(15)]


for i in range(15):
    dp[0][i] = i

for k in range(1,15):
    for n in range(1,15):
        dp[k][n] = dp[k-1][n] + dp[k][n-1]

for _ in range(T):
    K = int(input().strip())
    N = int(input().strip())
    print(dp[K][N])
