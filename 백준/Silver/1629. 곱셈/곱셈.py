import sys
input=sys.stdin.readline

a,b,c = map(int,input().split())

def multi (a,b):
    if b == 1:
        return a%c
    else:
        n = multi(a,b//2)
        if b % 2 == 0:
            return(n*n)%c
        else:
            return (n * n * a) % c

rst = multi(a,b)
print(rst)

