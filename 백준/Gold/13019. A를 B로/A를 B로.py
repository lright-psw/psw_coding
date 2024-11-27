a = list(input())
b = list(input())
cnt = 0
# 1. 무엇을 맨앞으로 가져갈지 선택을 해야해
# 무슨기준으로 해야할까 명확한 기준이 없다
# 위 아래 다른거 고르면 안됨?
# 뭘 옯기지 않아도 되는지 봐야함
g = list()

def error(a1, b1):
    if sorted(a1) != sorted(b1):
        return False
    return True 

e = error(a,b)

for i in range(len(b)-1,-1,-1):
    while a:
        last = a.pop()
        if b[i] == last:
            break
        else:
            g.append(last)

if e == False:
    print(-1)
else:
    print(len(g))