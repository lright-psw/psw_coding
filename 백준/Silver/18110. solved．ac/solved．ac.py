def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input().strip())

if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    cut = roundUp(n * 0.15)
    trimmed = arr[cut:n-cut]

    if not trimmed:
        print(0)
    else:
        avg = sum(trimmed) / len(trimmed)
        print(roundUp(avg))
