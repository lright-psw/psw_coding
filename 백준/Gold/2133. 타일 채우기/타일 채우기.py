import sys
input=sys.stdin.readline

N = int(input().rstrip())
if N%2 == 1: # 홀수일 경우
    print(0)
else:
    DP = [0] * (N+1)
    DP[2] = 3
    for i in range(4,N+1,2): # N까지 짝수만 DP값 구하기
        DP[i] = DP[i-2] * 3 + 2 # +2는 특이한 모양 2개 말하는거
        for j in range(2,i-2,2): # 점화식의 뒤에 시그마 부분 구하는 for문
            DP[i] += DP[j] * 2
    print(DP[N])

# 쉽게 설명이 안되는데....