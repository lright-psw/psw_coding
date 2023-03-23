import sys
input=sys.stdin.readline

N = int(input().rstrip())
wine = [] # 리스트가 아니라 배열로 선언시 stair_num = [0] * (N+1)
DP = [] # 리스트가 아니라 배열로 선언시 DP = [0] * (N+1)
#동적이라서 리스트가 압도적으로 편함
for _ in range(N):
    tmp = int(input().rstrip())
    wine.append(tmp)
if N<=2: 
    print(sum(wine))
else:
    DP.append(wine[0]) # DP[0] = wine[0]
    DP.append(wine[0] + wine[1]) # DP[1] = wine[0] + wine[1]
    DP.append(max(DP[1],wine[1] + wine[2],DP[0] + wine[2]))
    # DP[2] 설명들어갑니다
    # 아래의 점화식이 돌아가려면 DP[2] 즉 3번쨰 까지의 가장 큰 값이 베이스가 되어야함
    # 여기서 문제 발생 3번값은 2의3제곱 즉 8개 중 가장 큰값이 들어가야하는데 이를 전부 비교하는것은 바보짓
    # 따라서 추려내야함 (xxx, 000, XX0, X0X, 0XX, X00, 0X0, 00X, 000)
    # 이 중 00X 0X0, X00 만이 값이 될수 있음 (자세히 알고 싶으면 물어보셈)
    for i in range(3,N): # 세번째부터는 반복문으로 값을 구함
        a = wine[i] + wine[i-1] + DP[i-3] 
        b = wine[i] + DP[i-2] 
        DP.append(max(a,b,DP[i-1]))
    print(DP[-1])