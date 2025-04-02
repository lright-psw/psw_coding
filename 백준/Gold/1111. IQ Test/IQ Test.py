N = int(input())

# 다중 조건 분기 문제
# 1. 다음값이 무조건 1개임
# 2. 다음값이 여러개임 = A
# 3. 다음값을 구할 수 없음 = B
# 4. 만약 n이 1일때 A(구할 수 없음)
# 5. 만약 n이 2일때 (A 아님 두개의 값이 같을 경우 다음값 고정)
ptr = list(map(int, input().split()))

if N == 1:
    print("A")
elif N == 2:
    if ptr[0] == ptr[1]:
        print(ptr[1])
    else:
        print("A")
else:
    # a,b를 구해야함
    if (ptr[1] - ptr[0]) == 0:
        a = 0
    elif (ptr[2] - ptr[1]) % (ptr[1] - ptr[0]) != 0:
        print("B")
        exit()
    else:
        a = (ptr[2] - ptr[1]) // (ptr[1] - ptr[0])
    
    b = ptr[1] - (ptr[0] * a)

    flag =True
    for i in range(1,N):
        if ptr[i] != (ptr[i-1]*a) + b:
            flag =False
            break
    if(flag):
        print(ptr[-1]*a+b)
    else:
        print("B")

