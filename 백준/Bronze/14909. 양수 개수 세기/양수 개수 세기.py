arr =list(map(int,input().strip().split()))
cnt =0
for a in arr:
    if a>0:
        cnt +=1
print(cnt)