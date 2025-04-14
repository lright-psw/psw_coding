import sys

input = sys.stdin.readline

N = int(input().strip())
files = [input() for _ in range(N)]

pattern = ""

for i in range(len(files[0])):
    current_char = files[0][i]
    match = True
    for j in range(1, N):
        if files[j][i] != current_char:
            match = False
            break
    if match:
        pattern += current_char
    else:
        pattern += "?"

print(pattern)
