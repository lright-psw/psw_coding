from copy import deepcopy

# 방향: 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# CCTV 종류별 방향 조합
cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(board, y, x, dirs):
    for d in dirs:
        ny, nx = y, x
        while True:
            ny += dy[d]
            nx += dx[d]
            if not (0 <= ny < len(board) and 0 <= nx < len(board[0])):
                break
            if board[ny][nx] == 6:
                break
            if board[ny][nx] == 0:
                board[ny][nx] = '#'

def dfs(depth, board):
    global min_blind
    if depth == len(cctvs):
        cnt = sum(row.count(0) for row in board)
        min_blind = min(min_blind, cnt)
        return

    y, x, num = cctvs[depth]
    for dirs in cctv_dir[num]:
        copied = deepcopy(board)
        watch(copied, y, x, dirs)
        dfs(depth + 1, copied)

# 실제 사용자 입력 받기
N, M = map(int, input().split())
office = []
cctvs = []

for i in range(N):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))

min_blind = int(1e9)
dfs(0, office)

print(min_blind)
