# 나중에 다시 풀어보기 
import sys
input=sys.stdin.readline

iron_bar = list(input().rstrip())
stack = []
rst =0

for i in range(len(iron_bar)):
    if iron_bar[i] == '(':
        stack.append('(')
    elif iron_bar[i] == ')':
        if iron_bar[i-1] == '(':
            stack.pop()
            rst += len(stack)
        else:
            stack.pop()
            rst += 1
            
print(rst)