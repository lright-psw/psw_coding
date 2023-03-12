import sys
input=sys.stdin.readline

def fastExponentiation(a, x, n):    # a^x mod n
    y = 1
    while x > 0:
        if x & 1  == 1:         # 지수의 LSB가 1인지 확인
            y = (a * y) % n     # Multiply Operation
        a = (a * a) % n         # Square Operation
        x = x >> 1
    return y

a,b,c= map(int,input().split())
rst = fastExponentiation(a,b,c)

print(rst)

#알고리즘 출처
#https://velog.io/@choihocheol/%EB%B9%A0%EB%A5%B8-%EA%B1%B0%EB%93%AD%EC%A0%9C%EA%B3%B1-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98Fast-Exponentiation-Algorithm

#비트연산 모음
#https://dypar-study.tistory.com/15