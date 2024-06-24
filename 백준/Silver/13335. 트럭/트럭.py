# n은 다리를 건너는 트럭의 수
# w는 다리의 길이
# l은 다리의 최대하중
n,w,l = map(int, input().split())

truck = list(map(int,input().split()))

bri = [0] * w
cnt = 0
while len(bri) != 0:
    cnt += 1
    bri.pop(0)
    
    if truck:
        if sum(bri) + truck[0] <= l:
            bri.append(truck.pop(0))
        else:
            bri.append(0)
print(cnt)