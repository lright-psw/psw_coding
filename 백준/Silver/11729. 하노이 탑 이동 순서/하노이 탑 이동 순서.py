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

#출처
#https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-python-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9Chanoi-top-in-python