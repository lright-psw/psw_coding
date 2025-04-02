import sys
from math import factorial, gcd
from collections import Counter
from functools import lru_cache
input = sys.stdin.readline

# 미리 팩토리얼 저장
fact = [1] * 21
for i in range(1, 21):
    fact[i] = fact[i-1] * i

# N의 모든 정수 분할 (사이클 분해)
def generate_partitions(n, i=1):
    if n == 0:
        yield []
    for k in range(i, n+1):
        for rest in generate_partitions(n - k, k):
            yield [k] + rest

# 해당 사이클 분해에 대한 순열 수 계산
def count_permutations_by_cycle_type(part):
    n = sum(part)
    counter = Counter(part)
    denom = 1
    for cycle_len in counter:
        denom *= (cycle_len ** counter[cycle_len]) * fact[counter[cycle_len]]
    return fact[n] // denom

# 기약 분수 출력
def reduce_fraction(a, b):
    g = gcd(a, b)
    a //= g
    b //= g
    return f"{a}" if b == 1 else f"{a}/{b}"

T = int(input())
for _ in range(T):
    W, H, S = map(int, input().split())
    N = W * H

    win = 0
    total = fact[N]

    for part in generate_partitions(N):
        cycles = len(part)
        min_swaps = N - cycles
        if min_swaps < S:
            win += count_permutations_by_cycle_type(part)

    print(reduce_fraction(win, total))
