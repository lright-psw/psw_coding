N = int(input())

comb = 1
rst = 1
while N > comb:
    comb += 6 * rst
    rst += 1

print(rst)
