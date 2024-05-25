x = int(input())
n =1

while x> n:
    x-=n
    n+=1

if n % 2 != 0:
    a = n
    b = 1
    for i in range(x-1):
        a-=1
        b+=1
else:
    a = 1
    b = n
    for i in range(x-1):
        a+=1
        b-=1
print(f"{a}/{b}")