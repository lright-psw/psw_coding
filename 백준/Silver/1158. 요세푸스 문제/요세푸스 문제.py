import sys
from collections import deque
input=sys.stdin.readline

n, k = map(int,input().split())
queue = deque([i for i in range(1,n+1)])
ptr = []

while queue:
    queue.rotate(-(k-1))
    ptr.append(queue.popleft())
print(f'<{", ".join(map(str,ptr))}>')

