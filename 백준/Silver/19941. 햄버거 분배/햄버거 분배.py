import sys
input = sys.stdin.readline

N,K = map(int, input().split())
arr = list(input())
cnt = 0
for i in range(N):
    if arr[i] == 'P':
        #i+k+1인 이유는 반복문의 범위 설정은 '미만'의 개념이기 때문에 +1을 해줌
        for j in range(max(i-K,0),min(i+K+1,N)): 
            if arr[j] == 'H':
                arr[j] = 0
                cnt += 1
                break
print(cnt)