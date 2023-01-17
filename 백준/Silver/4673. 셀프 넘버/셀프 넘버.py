ptr = list(range(1,10001))

num = [0] * 10001

for i in ptr:
    for j in str(i):
        i += int(j)
    if i < 10001:
        num[i] = 1
        
for i in range(1,10001):
    if num[i] == 0:
        print(i)
