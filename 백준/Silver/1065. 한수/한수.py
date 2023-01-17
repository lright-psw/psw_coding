# 연속하는 두 항의 차이가 모두 일정한 수열을 뜻한다. 
# 10부터 99까지는 전부 등차수열임
# 1~9까지는 그 자체로 수열임

num = int(input())
sum = 0
for i in range(1,num+1):
    ptr=list(map(int,str(i)))
    if i < 100:
        sum += 1
    elif ptr[1]-ptr[0] == ptr[2]-ptr[1]:
        sum += 1
        
print(sum)
