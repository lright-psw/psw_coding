import sys
n = int(input())
ptr =[]

for i in range(n):
    ptr.append(int(sys.stdin.readline()))
ptr.sort(reverse=False)

for i in range(len(ptr)):
    print(ptr[i])