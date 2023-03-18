import sys
input=sys.stdin.readline


T = int(input().rstrip())
for _ in range(T):
    DP = []
    for _ in range(3):
        DP.append(1)
    for _ in range(2): 
        DP.append(2)
    N = int(input().rstrip())
    if N <= 5:
        print(DP[N-1])
        continue
    for i in range(5,N):
        DP.append(DP[i-1] + DP[i-5])
    print(DP[-1])