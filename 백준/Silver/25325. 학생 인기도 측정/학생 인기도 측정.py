import sys
input=sys.stdin.readline


N = int(input().rstrip())

dic = {}
for i in input().split():
    dic[i] = 0
for _ in range(N):
    for i in input().split():
        dic[i] += 1
        
for i in sorted(dic.items(), key =lambda x:(-x[1],x[0])):
    print(*i)