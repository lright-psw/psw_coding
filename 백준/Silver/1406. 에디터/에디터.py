

# 다른사람풀이
# 문자열을 스택에 두개로 쪼개서 나누어 담는 것 감탄밖에 안나온다..
import sys
input=sys.stdin.readline

cur1 = list(input().rstrip())
cur2 = []
n = int(input())

for i in range(n) :
    cmd = list(input().split())
    if cmd[0] == 'L':
        if cur1:
            cur2.append(cur1.pop())
    elif cmd[0] == 'D':
        if cur2:
            cur1.append(cur2.pop())
    elif cmd[0] == 'B':
        if cur1:
            cur1.pop()
            
    else:
        cur1.append(cmd[1])
        
cur1.extend(reversed(cur2))
print(''.join(cur1))




# 내가 풀었던 풀이 
# 시간초과로 실패 insert ,remove를 사용하면 시간초과 발생 
# import sys
# input=sys.stdin.readline

# ptr = list(input().rstrip())
# cur = len(ptr)
# n = int(input())

# for i in range(n) :
#     cmd = list(input().split())
#     if cmd[0] == 'L':
#         if cur >0:
#             cur-=1
#     elif cmd[0] == 'D':
#         if cur < len(ptr):
#             cur+=1
#     elif cmd[0] == 'B':
#         if cur >0:
#             ptr.remove(ptr[cur-1])
#     elif cmd[0] == 'P':
#         ptr.insert(cur, cmd[1])
#         cur += 1

# print(''.join(ptr))