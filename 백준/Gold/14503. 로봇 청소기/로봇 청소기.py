# 0 3 2 1순으로 돌아감 북 서 남 동
# 0 1 2 3 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
room = []
visited = []

n,m = map(int, input().split())

r, c, d = map(int,input().split())

for _ in range(n):
    room.append(list(map(int,input().split())))

for _ in range(n):
    visited.append(list(0 for _ in range(m)))

# 0 : 청소되지 않은 칸 1: 청소된 칸
# 1 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
#   2-1 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#   2-2 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
#   2-3 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
#       2-3-1 반시계 방향으로 90도로 회전한다.
#       2-3-2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
#       2-3-3 1번으로 돌아간다.

visited[r][c] = 1
cnt = 1

while True:
    flag = 0            
    for _ in range(4):  
        d = (d+3) % 4   
        x = r + dx[d]
        y = c + dy[d]

        if 0 <= x < n and 0 <= y < m and room[x][y] == 0:
            if visited[x][y] == 0:
                visited[x][y] = 1
                cnt += 1
                r = x
                c = y
                flag = 1
                break

    if flag == 0: 
        if room[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]