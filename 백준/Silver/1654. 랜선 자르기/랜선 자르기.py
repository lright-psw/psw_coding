K, N = map(int, input().strip().split())

arr = [int(input()) for _ in range(K)]

low = 1
high = max(arr)
rst = 0

while low <= high:
    mid = (low + high) // 2
    count = 0
    for a in arr:
        count += a // mid

    if count >= N:
        rst = mid
        low = mid + 1
    else:
        high = mid - 1

print(rst)
