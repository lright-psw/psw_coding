import sys
input=sys.stdin.readline


def pig(p):
    tmp = []
    for i in range(len(p)):
        cnt = 0
        for j in range(len(p)):
            if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
                cnt+=1
        tmp.append(cnt + 1)
    return tmp


N = int(input().rstrip())
ptr = []
for i in range(N):
    ptr.append(list(map(int,input().split())))
rst = pig(ptr)
for i in rst:
    print(i,end=' ')

