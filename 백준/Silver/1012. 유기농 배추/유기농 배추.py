# 유기농 배추
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

cnt = 0

def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >=N or ny >= M:
                continue

            if arr[nx][ny] == 1:
                dq.append((nx,ny))
                arr[nx][ny] = 0

for _ in range(n):
    M,N,K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        x,y = map(int,input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt +=1
    print(cnt)