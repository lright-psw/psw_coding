import sys
input=sys.stdin.readline

n=int(input().rstrip())
ptr = []
rst = []
cnt = 1
err = 0
for i in range(n):
    a = int(input().rstrip())
    while cnt <= a:
        ptr.append(cnt)
        rst.append('+')
        cnt+=1
    
    if ptr[-1] == a:
        ptr.pop()
        rst.append('-')
    else:
        print("NO")
        err = 1
        break
    
if err == 0:
    for i in rst:
        print(i)