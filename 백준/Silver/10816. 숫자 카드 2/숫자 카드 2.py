N = int(input().strip())
card = {}

ptr = list(map(int, input().strip().split()))

for p in ptr:
    if p not in card:
        card[p] = 1
    else:
        card[p] += 1

M = int(input().strip())

ptr = list(map(int, input().strip().split()))

for p in ptr:
    if p not in card:
        print(0, end=" ")
    else:
        print(card[p], end=" ")
