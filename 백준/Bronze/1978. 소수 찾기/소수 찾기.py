import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
arr = list(map(int, input().strip().split()))

cnt = 0
for a in arr:
    if is_prime(a):
        cnt += 1

print(cnt)
