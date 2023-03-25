import sys
input=sys.stdin.readline

N = int(input().rstrip())
DP = [i for i in range(N+1)] # 모든수를 1의 제곱의 합으로 항의 개수를 맞춤
# DP를 1번부터 저장하면 안됨 0일떄는 0개라고 알려주는 것도 필요해서 0~N+1개로 DP를 설정해야함 계속 틀림
for i in range(1,N+1): # 이건 계산이구요 
    for j in range(1,i): # 이건 뺴주는 과정인데 궁금하면 물어보시고
        if j*j > i:
            break
        if DP[i] > DP[i-(j*j)]+1: # DP[i-j*j]+1에서 1은 j*j로 인해 빠진 값을 항의 개수로 넣어주는거
            DP[i] = DP[i-(j*j)]+1
# 시간 오류 났다 ㅠ
# 인터넷 뒤져보니깐 min함수 시간복잡도가 n이라던데 "DP[i] = min(DP[i],DP[i-(j*j)]+1):"
# 그럼 위에 2중포문 안에 들어있는 내 코드는 n의 3제곱짜리 시간복잡도를 가지는 거다.
# 이거보다 작게 할 방법이 모르겠네...
# 찾았다 보니깐 if문을 사용하면 이게 상수취급을 해서 시간복잡도를 n의 제곱까지 낮출 수 있다.
print(DP[N])