import sys
input=sys.stdin.readline

n=int(input())
stack=[]
for i in range(n):
    ptr = input().split()
    if ptr[0] == 'push':
        stack.append(ptr[1])
    elif ptr[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ptr[0] == 'size':
        print(len(stack))
    elif ptr[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ptr[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])