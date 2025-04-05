N, K = map(int, input().split())

A_set = set()
for _ in range(N):
    A_set.add(int(input().strip()))

A_list = sorted(A_set, reverse=True) 

rst = 0
for A in A_list:
    if A > K:
        continue
    rst += K // A
    K %= A

print(rst)
