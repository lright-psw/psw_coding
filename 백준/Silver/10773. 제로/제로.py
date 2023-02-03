import sys
input=sys.stdin.readline


n=int(input())
stack=[]
for i in range(n):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
    
print(sum(stack))