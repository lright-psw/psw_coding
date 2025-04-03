import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    parts = input().split()
    command = parts[0]

    if command == "add":
        S.add(int(parts[1]))
    elif command == "remove":
        S.discard(int(parts[1]))
    elif command == "check":
        print(1 if int(parts[1]) in S else 0)
    elif command == "toggle":
        x = int(parts[1])
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif command == "all":
        S = set(range(1, 21))
    elif command == "empty":
        S.clear()

