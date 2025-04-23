import math

A,B,V = map(int,input().strip().split())

rst = math.ceil((V-B)/(A-B))
print(rst)