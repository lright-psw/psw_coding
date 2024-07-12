from collections import deque
from itertools import combinations
n,k = map(int,input().split())

home = []
inf = float('inf')
rst = inf

for i in range(n):
    home.append(list(map(int,input().split())))

for c in combinations(range(n),k):
    tmp = 0
    for i in range(n):
        h = home[i]
        comb = [home[c[a]] for a in range(k)]
        m = inf
        for j in comb:
            distance = abs(h[0]-j[0]) + abs(h[1]- j[1])
            m = min(m,distance)
        tmp = max(tmp,m)
    rst = min(tmp,rst)
print(rst)