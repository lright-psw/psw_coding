import sys
from collections import deque

# 정답 메모 테이블
answer_note = {}

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 사전 계산 BFS: 목표 상태 "123456789" (9 = 빈칸)
def BFS():
    queue = deque()
    start = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    queue.append((start, 0, 8))  # 퍼즐 상태, 거리, 빈칸 위치
    answer_note[''.join(start)] = 0

    while queue:
        cur_state, cur_cnt, cur_pos = queue.popleft()
        cur_row, cur_col = divmod(cur_pos, 3)

        for dx_i, dy_i in zip(dx, dy):
            nx, ny = cur_col + dx_i, cur_row + dy_i
            if 0 <= nx < 3 and 0 <= ny < 3:
                next_pos = ny * 3 + nx
                next_state = cur_state[:]
                next_state[cur_pos], next_state[next_pos] = next_state[next_pos], next_state[cur_pos]
                next_str = ''.join(next_state)
                if next_str not in answer_note:
                    answer_note[next_str] = cur_cnt + 1
                    queue.append((next_state, cur_cnt + 1, next_pos))

# inversion check로 풀 수 있는 퍼즐인지 확인
def is_solvable(puzzle_str):
    arr = puzzle_str.replace('9', '')
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0

# BFS 사전 계산 먼저 수행
BFS()

# 테스트케이스 수
n = int(sys.stdin.readline())
for _ in range(n):
    puzzle = []

    # 중간 빈 줄 무시
    while True:
        line = sys.stdin.readline()
        if line.strip():  # 비어 있지 않은 줄이면
            puzzle.append(line.strip())
            if len(puzzle) == 3:
                break

    # '#' → '9'로 치환
    puzzle_str = ''
    for row in puzzle:
        for ch in row:
            puzzle_str += '9' if ch == '#' else ch

    # 가능한 퍼즐인지 확인 후 출력
    if is_solvable(puzzle_str):
        print(answer_note.get(puzzle_str, "impossible"))
    else:
        print("impossible")
