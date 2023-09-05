import sys
input = sys.stdin.readline

N,L = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
rst = 0

def check(line):
    for i in range(1,N):
        if abs(line[i]-line[i-1]) > 1: # 1차이만 가능
            return False
        if line[i] < line[i-1]: # 현재<이전, 경사로를 만들기 위해 오른쪽을 스캔함(낮은 곳에 경사로 설치)
            for j in range(L):
                if i+j >= N or visit[i+j] or line[i] != line[i+j]: # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
                    return False
                if line[i] == line[i+j]:
                    visit[i+j] = 1
        elif line[i] > line[i-1]: # 현재>이전, 경사로를 만들기 위해 왼쪽을 스캔함
            for j in range(L):
                # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
                # '-1'해주는 이유 j가 0부터 시작하기 떄문에
                if i-j-1 < 0 or visit[i-j-1] or line[i-1] != line[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    visit[i-j-1] = 1
    return True

for i in range(N):
    visit = [False for _ in range(N)]
    if check([arr[i][j] for j in range(N)]):
        rst += 1

for j in range(N):
    visit = [False for _ in range(N)]
    if check([arr[i][j] for i in range(N)]):
        rst += 1
print(rst)