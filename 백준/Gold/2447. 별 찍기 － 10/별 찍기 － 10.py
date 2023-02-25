import sys
from collections import deque
input=sys.stdin.readline


def draw(n):
    ptr = []
    for i in range(3*len(n)):
        if i // len(n) == 1:
            ptr.append(n[i%len(n)] + " " * len(n) + n[i%len(n)])
        else:
            ptr.append(n[i%len(n)] * 3)
    return ptr


star = ["***", "* *", "***"]    
N = int(input().rstrip())
cnt = 0

while N != 3:       
    N = N // 3
    cnt += 1        

for _ in range(cnt):	
    star = draw(star)   

for i in star:      
    print(i)



#출처
#https://velog.io/@hrzo1617/%EB%B0%B1%EC%A4%80-2447-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B3%84-%EC%B0%8D%EA%B8%B0-10

