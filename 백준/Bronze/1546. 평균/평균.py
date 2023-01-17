cnt = int(input())
ptr = list(map(int,input().split()))
a=0
b=0

for i in ptr[0:]:
    if a<i:
        a=i

for i in ptr[0:]:
    b+=float(i/a*100)

print(f'{b/cnt}')
