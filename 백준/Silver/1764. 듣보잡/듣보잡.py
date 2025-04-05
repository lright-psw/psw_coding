import sys
input = sys.stdin.readline

N, M = map(int, input().split())

h = set()
for _ in range(N):
    h.add(input().strip())

rst = []
for _ in range(M):
    s = input().strip()
    if s in h:
        rst.append(s)


print(len(rst))
for name in sorted(rst):
    print(name)
