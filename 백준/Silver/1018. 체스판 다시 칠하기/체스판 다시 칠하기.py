N, M = map(int, input().strip().split())

board = [input().strip() for _ in range(N)]


def check(y, x):
    patterns = ["WB", "BW"]
    min_paint = 64

    for first_color in ["W", "B"]:
        count = 0
        for i in range(8):
            for j in range(8):
                now = patterns[(i + j) % 2][0 if first_color == "W" else 1]
                if board[y + i][x + j] != now:
                    count += 1
        min_paint = min(min_paint, count)
    return min_paint


result = 64
for i in range(N - 7):
    for j in range(M - 7):
        result = min(result, check(i, j))

print(result)
