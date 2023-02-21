import sys
from collections import deque
input=sys.stdin.readline

def fibo(k):
    if k==0:
        return 0
    elif k<=2:
        return 1
    return fibo(k-1) + fibo(k-2)


n= int(input().rstrip())
print(fibo(n))