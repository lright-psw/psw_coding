import sys
from collections import deque
input = sys.stdin.readline

# 상 하 좌 우
distance = [(-1,0),(1,0),(0,-1),(0,1)]

# T 모양 정의
T_shapes = [
    [(-1,0),(0,-1),(0,0),(0,1)],
    [(-1,0),(0,-1),(0,0),(1,0)],
    [(0,-1),(0,0),(1,0),(0,1)],
    [(-1,0),(0,0),(1,0),(0,1)],
            ]

N,M = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(N)]


rst =0

def bfs(i,j):
    global rst
    dq = deque()
    dq.append((i,j,arr[i][j],1,{(i,j)}))

    while dq:
        y,x,cost,depth,visited_set = dq.popleft()

        if depth ==4:
            rst = max(rst,cost)
            continue
        
        for dy,dx in distance:
            nx = dx+x
            ny = dy+y
            if nx>=0 and nx<M and ny>=0 and ny<N and (ny,nx) not in visited_set:
                dq.append((ny,nx,cost + arr[ny][nx],depth+1,visited_set | {(ny,nx)}))


def Ttetromino(i,j):
    global rst
    for shape in T_shapes:
        tmp = 0
        flag = True
        for dy,dx in shape:
            nx= j + dx
            ny= i + dy
            if nx>=0 and nx<M and ny>=0 and ny<N:
                tmp += arr[ny][nx]
            else:
                flag =False
                break
        if flag:
            rst = max(rst,tmp)

def main():
    for i in range(N):
        for j in range(M):
            # 완전탐색 'ㅜ'제외
            bfs(i,j)
            # 'ㅜ' 탐색
            Ttetromino(i,j)
    print(rst)


if __name__=='__main__':
    main()
