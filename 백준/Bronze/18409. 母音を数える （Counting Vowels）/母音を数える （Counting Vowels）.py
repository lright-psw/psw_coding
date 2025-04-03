s = int(input())
N = list(input())

cnt =0

for n in N:
    if n =='a' or n == 'i'or n == 'u'or n == 'e'or n == 'o':
        cnt+=1

print(cnt)


