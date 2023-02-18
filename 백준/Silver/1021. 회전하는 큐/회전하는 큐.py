import sys
from collections import deque
input=sys.stdin.readline

n, k = map(int,input().split())
want = list(map(int,input().split()))
queue = deque([i for i in range(1,n+1)])
atm = 0

for i in want:
    while queue:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) > len(queue)/2:
                queue.rotate(1)
                atm+=1
            else:
                queue.rotate(-1)
                atm+=1

print(atm)