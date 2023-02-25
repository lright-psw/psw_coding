import sys
from collections import deque
input=sys.stdin.readline

n= int(input().rstrip())
queue = deque(enumerate(map(int,input().split())))
rst = []
for i in range(n):
    balloon, move = queue.popleft()
    rst.append(balloon+1)
    if move>0:
        queue.rotate(-(move-1))
    elif move<0:
        queue.rotate(-move)
print(' '.join(map(str,rst)))