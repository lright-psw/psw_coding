N = int(input())

line = list(map(int,input().strip().split()))

line.sort()

rst =0
cnt =0

for p in line:
    cnt+=p
    rst+=cnt
print(rst)