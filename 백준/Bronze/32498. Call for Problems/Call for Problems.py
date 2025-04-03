n = int(input())
excluded = 0

for _ in range(n):
    d = int(input())
    if d % 2 == 1:  # 홀수
        excluded += 1

print(excluded)
