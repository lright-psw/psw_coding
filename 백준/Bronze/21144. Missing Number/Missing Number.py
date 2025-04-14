import sys

input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

numbers = [str(i) for i in range(1, n + 1)]

for i in range(1, n + 1):
    test = numbers.copy()
    test.remove(str(i))
    joined = "".join(test)
    if joined == s:
        print(i)
        break
