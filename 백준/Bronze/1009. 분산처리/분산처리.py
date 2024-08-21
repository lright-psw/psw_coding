n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    rst = a%10
    
    if rst == 0:
        print(10)
    elif rst == 1 or rst == 5 or rst == 6:
        print(rst)
    elif rst == 4 or rst ==9:
        if b%2 ==0:
            print((rst**2)%10)
        else:
            print(rst)
    else:
        if b%4 == 0:
            print((rst**4)%10)
        else:
            print((rst**(b%4))%10)