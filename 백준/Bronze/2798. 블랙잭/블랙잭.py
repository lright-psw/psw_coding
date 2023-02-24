import sys
input=sys.stdin.readline

n, m = map(int,input().split())
black = list(map(int,input().split()))

rst = 0
for i in black:
    for j in black:
        for k in black:
            if i==j or i==k or j==k:
                continue
            cnt = i+j+k
            if m>=cnt and cnt > rst:
                rst = cnt
    
print(rst)