#1번 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. = 2초 
#2번 인벤토리에서 블록 하나를 꺼내어 가장 위에 있는 블록 위에 놓는다 = 1초

#땅의 높이는 256블록을 초과할 수 없음
import math

n,m,b = map(int,input().split())

rst = []

#평지화 할 땅 
ground = []

#맵 입력받기
for _ in range(n):
    ground.extend(list(map(int,input().split())))

for h in range(257):
    tmp_b=b
    time = 0
    for g in ground:
        #높이가 땅보다 높을때
        if h > g:
            time += abs(h-g)
            tmp_b -= abs(h-g)
        #높이가 땅보다 낮을때
        elif h < g:
            time += (abs(h-g))*2
            tmp_b += abs(h-g)
    if tmp_b < 0:
        continue
    rst.append(time)

min_time = math.inf 
min_hight = -1

for hight,time in enumerate(rst):
    if time <= min_time:
        min_time = time
        min_hight = hight

print(f"{min_time} {min_hight}")