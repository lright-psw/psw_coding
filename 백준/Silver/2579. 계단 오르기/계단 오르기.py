import sys
input=sys.stdin.readline

N = int(input().rstrip())
stair_num = [] # 리스트가 아니라 배열로 선언시 stair_num = [0] * (N+1)
DP = [] # 리스트가 아니라 배열로 선언시 DP = [0] * (N+1)
#동적이라서 리스트가 압도적으로 편함
DP.append(0) #처음 시작지점
for _ in range(N):
    tmp = int(input().rstrip())
    stair_num.append(tmp)
if N<=2:  #만약 계단이 2개 이하이면 그냥 더해서 출력ㄱ
    print(sum(stair_num))
else:
    DP.append(stair_num[0]) #첫번쨰 계단
    DP.append(stair_num[0] + stair_num[1]) #두번째 계단
    for i in range(3,N+1): # 세번째부터는 반복문으로 값을 구함
#??: 왜 N+1이냐면 시작지점을 0으로 잡아야해서 마지막 계단이 6번 배열에 들어감
# 그래서 N으로 할 경우 마지막 계단을 계산할 수 없음
        a = stair_num[i-1] + stair_num[i-2] + DP[i-3] #도착할 계단 바로 이전 계단을 밟았을경우
        b = stair_num[i-1] + DP[i-2] #도착할 계단 바로 이전 계단을 밟지 않았을경우
        if a>=b: # 높은 숫자를 배열의 저장
            DP.append(a)
        else: 
            DP.append(b)
    print(DP[-1])