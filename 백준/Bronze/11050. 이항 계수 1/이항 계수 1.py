N, K = map(int, input().strip().split())


def fact(n):
    cnt = 1
    for i in range(1, n + 1):
        cnt *= i
    return cnt


if K < 0:
    print(0)
elif K > N:
    print(0)
else:
    print(int(fact(N) / (fact(K) * fact(N - K))))
