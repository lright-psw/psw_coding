import sys
input=sys.stdin.readline


n=int(input())
for i in range(n):
    ps = input()
    cnt = 0
    for j in range(len(ps)):
        if ps[j] == '(':
            cnt+=1
        elif ps[j] == ')':
            cnt-=1
        if cnt<0:
            print("NO")
            break
    if cnt == 0:
        print("YES")
    elif cnt>0:
        print("NO")