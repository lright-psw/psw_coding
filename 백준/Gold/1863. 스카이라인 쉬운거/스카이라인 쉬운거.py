n = int(input())

arr =[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

skyline = []
cnt = 0
for x,y in arr:
    while len(skyline)>0 and skyline[-1] > y:
        skyline.pop()
        cnt+=1
    if len(skyline)>0 and skyline[-1] == y:
        continue
    else:
        skyline.append(y)
while len(skyline) > 0 and skyline[-1] != 0:
    if skyline[-1]>0:
        skyline.pop()
        cnt+=1
print(cnt)
