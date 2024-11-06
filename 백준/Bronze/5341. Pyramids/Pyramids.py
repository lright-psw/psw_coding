while True:
    n = int(input())
    rst = 0
    if  n == 0:
        break
    for i in range(1,n+1):
        rst+=i
    print(rst)