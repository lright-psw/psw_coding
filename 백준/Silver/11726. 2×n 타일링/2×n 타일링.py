import sys
input=sys.stdin.readline

N = int(input().rstrip())
DP = []
DP.append(1) # 2 * 1
DP.append(2) # 2 * 2
for i in range(2,N+1): # 2 * 3 이상부터는 점화식으로 계산 
    DP.append((DP[i-1]+DP[i-2])%10007) 
print(DP[N-1]) # 한번더 돌아서 N-1