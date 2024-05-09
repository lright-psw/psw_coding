import sys
input = sys.stdin.readline

n = int(input());

color = []

for _ in range(n):
    color.append(list(map(int,input().split())))

for i in range(1,n): 
    #박아보고 안것 아래서부터 올라오는 식으로 코드를 작성하면 원본값이 훼손되어 이상한 답이 나온다.
    #무조건 위에서 내려가는 식으로 짜거나 원본값을 따로 저장해줄 무언가가 필요하다.
    
    #이번 선택이 빨간색일때
    color[i][0] = min(color[i-1][1],color[i-1][2]) + color[i][0]
    #이번 선택이 초록색일때
    color[i][1] = min(color[i-1][0],color[i-1][2]) + color[i][1]
    #이번 선택이 파란색일때
    color[i][2] = min(color[i-1][0],color[i-1][1]) + color[i][2]
    
sum_min = min(color[n-1][0],color[n-1][1],color[n-1][2])
print(sum_min)