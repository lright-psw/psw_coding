rst =0
for i in range(2):
    a,b,c,d = map(int,input().split())
    tmp = a+b+c+d
    rst = max(tmp,rst)
print(rst)
