import sys
from itertools import permutations
input=sys.stdin.readline


N = int(input().rstrip())
K = int(input().rstrip())
ptr =  []
for i in range(N):
    ptr.append(int((input().rstrip())))

rst = set()
for p in permutations(ptr,K):
    rst.add(''.join(map(str,p)))

print(len(rst))
