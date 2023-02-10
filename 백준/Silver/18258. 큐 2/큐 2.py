import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
queue=deque()
for i in range(n):
    ptr = input().split()
    if ptr[0] == 'push':
        queue.append(ptr[1])
    elif ptr[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif ptr[0] == 'size':
        print(len(queue))
    elif ptr[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif ptr[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif ptr[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])