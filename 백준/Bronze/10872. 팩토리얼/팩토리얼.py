import sys
from collections import deque
input=sys.stdin.readline

n= int(input().rstrip())
cnt = 1
for i in range(1,n+1):
    cnt *= i
print(cnt)