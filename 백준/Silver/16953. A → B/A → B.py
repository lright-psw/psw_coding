import sys

input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0
if a == b:
    print(1)
else:
    while True:
        cnt += 1
        tmp = b
        if int(b) % 10 == 1:
            b //= 10
        elif int(b) % 2 == 0:
            b /= 2
        if tmp == b:
            cnt = -1
            break
        elif a == b:
            cnt += 1
            break
    print(cnt)
