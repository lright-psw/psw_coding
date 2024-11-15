l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = 0
m =0

if a%c == 0:
    k = a//c
else:
    k = (a//c) +1

if b%d == 0:
    m = b//d
else:
    m = (b//d) +1
    
print(l-max(k,m))