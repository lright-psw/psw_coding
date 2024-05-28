from collections import deque

T= int(input())

for i in range(T):
    flag=1
    reverse = 0
    p = input()
    n = int(input())
    arr = input().strip()
    dq  = deque(arr[1:-1].split(','))
    #print(dq)
    # []이면 dq = deque()로 아무것도 없는걸로 입력
    if n == 0:
        dq = deque()
    # 계산
    for i in p:
        if i == "R":
            reverse +=1
        elif i == "D":
            if not dq :
                print("error")
                flag =0
                break
            elif reverse % 2 == 0:
                dq.popleft()
            elif reverse % 2 != 0:
                dq.pop()
    if flag==1 and reverse % 2 != 0:
        dq.reverse()
        print("["+",".join(dq)+"]")
    elif flag==1 and reverse % 2 == 0:
        print("["+",".join(dq)+"]")