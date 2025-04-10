import sys
from collections import deque
input = sys.stdin.readline



# 1. 경계 밖으로 나가서는 안됨
# 2. 칸의 경계와 일치하게 붙여야 한다
# 3. 0이 적힌 칸에는 색종이가 있으면 안 된다
# 4. 불가능 하다면, -1을 출력

def main():
    board = [list(map(int, input().split())) for _ in range(10)]
    paper = [0, 5, 5, 5, 5, 5]  # 인덱스 1~5: 색종이 개수 0번 자리는 그냥 안쓸거임
    tmp = float('inf')

    # 종이를 붙이는 곳에 3번 조건이 맞는지 확인하는 함수수
    def is_possible(y,x,size):
        if y+size > 10 or x+size>10:
            return False

        for i in range(y,y+size):
            for j in range(x,x+size):
                if board[i][j] != 1:
                    return False
        return True

    # 종이 세팅
    def set_paper(y,x,size,v):
        for i in range(y,y + size):
            for j in range(x,x + size):
                board[i][j] = v

    def dfs(lv):
        nonlocal tmp
        # 종료 조건
        if lv >= tmp:
            return

        # 가지
        for i in range(10):
            for j in range(10):
                if board[i][j] == 1:
                    for size in range(5,0,-1):
                        # 종이의 인덱스가 5~1까지만 돌아가고 종이를 붙일수 있는지 확인 해야하는데 이걸 따로 뺄까?
                        if paper[size] > 0 and is_possible(i,j, size):
                            paper[size] -= 1
                            set_paper(i,j,size,0)
                            dfs(lv+1)
                            set_paper(i,j,size,1)
                            paper[size] += 1
                    return
        tmp = min(tmp, lv)

    dfs(0)
    rst = tmp if tmp != float('inf') else -1
    print(f"{rst}")

if __name__=='__main__':
    main()