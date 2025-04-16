N = int(input())
arr = list(map(int, input().strip().split()))
t, p = map(int, input().strip().split())

cnt = 0
for a in arr:
    cnt += (a + t - 1) // t

print(cnt)

print(f"{N//p} {N%p}")
