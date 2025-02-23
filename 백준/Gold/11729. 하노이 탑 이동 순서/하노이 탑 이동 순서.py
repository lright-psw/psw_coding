import sys
input=sys.stdin.readline

def hanoi(n,st,nd,rd):
    if n == 1:
        ptr.append([st,rd])
    else:
        hanoi(n-1,st,rd,nd)
        ptr.append([st,rd])
        hanoi(n-1,nd,st,rd)


ptr=[]
N = int(input().rstrip())
hanoi(N,1,2,3)
print(len(ptr))
print("\n".join([' '.join(str(i) for i in row) for row in ptr]))
