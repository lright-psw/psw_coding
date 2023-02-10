import sys
from collections import deque
input=sys.stdin.readline

n = int(input().rstrip())
queue = deque([i for i in range(1,n+1)])

for i in range(n):
    if len(queue) == 1:
        print(queue[0])
        break
    else:
        queue.popleft()
        queue.append(queue[0])
        queue.popleft()
        

# 공식을 만들어서 품
# input = int(input())
# square = 2

# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break