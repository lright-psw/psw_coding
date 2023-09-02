import sys
input=sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    arr.append(list(map(int,input().split())))

def bfs(i,j):
    q = deque()
    tmp = []
    q.append((i,j))
    tmp.append((i,j))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    tmp.append((nx, ny))
    return tmp

rst = 0
while True: 
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                
                if len(country) > 1:
                    flag = 1
                    number = sum([arr[x][y] for x,y in country]) // len(country)
                    for x,y in country:
                        arr[x][y] = number
    if flag == 0:
        break
    rst += 1
print(rst)
