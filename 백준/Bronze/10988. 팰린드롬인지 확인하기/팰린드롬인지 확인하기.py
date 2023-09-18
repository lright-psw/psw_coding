import sys
input = sys.stdin.readline

a = input().rstrip()

b = a[::-1]

if a==b:
    print(1)
else:
    print(0)