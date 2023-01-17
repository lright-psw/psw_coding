cnt = int(input())

for _ in range(cnt):
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]
    a = 0
    for i in num[1:]:
        if i > avg:
            a += 1
    b = a/num[0]*100
    print('%.3f'%b+'%')
    