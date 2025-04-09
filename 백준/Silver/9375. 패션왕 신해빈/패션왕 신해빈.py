t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    print(result - 1)
