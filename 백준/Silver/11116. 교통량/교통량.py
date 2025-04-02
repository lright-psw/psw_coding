T = int(input())

# 왼쪽 앞, 왼쪽 뒤, 오른쪽 앞, 오픈쪽 뒤

for _ in range(T):
    cnt = 0
    n = int(input())
    left_times = list(map(int, input().split()))
    right_times = list(map(int, input().split()))

    right_times = set(right_times)
    
    for i in left_times:
        if (i+1000 in right_times) and  (i+1500 in right_times):
            cnt+=1
    print(cnt)