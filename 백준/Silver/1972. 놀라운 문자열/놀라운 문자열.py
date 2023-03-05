import sys
input=sys.stdin.readline

while True:
    N= input().rstrip()
    if N == "*":
        break
    for i in range(1,len(N)-1):
        arr = set()
        for j in range(len(N)-i):
            a = N[j] + N[i+j]
            if a in arr:
                print(N,"is NOT surprising.")
                break
            else:
                arr.add(a)
        else:
            continue
        break
    else:
        print(N,"is surprising.")