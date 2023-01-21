import sys

rst=0
n=int(input())
arr = [[0 for col in range(101)]for row in range(101)]
#arr = [[0]*101 for in range(101)] 으로도 선언 가능

for i in range(n): #입력된 값만큼 반복
    x, y = map(int,input().split()) # 색종이를 붙인 위치인 두 개의 자연수를 정수형으로 받음
    
    # 그래프(맵)에 색종이를 붙인 위치를 표시 색종이는 10*10 크기임으로 입력받은 정수의 값에 10을 더해준만큼 반복
    for r in range(x,x+10): 
        for c in range(y,y+10):
            arr[r][c] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            rst += 1

print(rst)