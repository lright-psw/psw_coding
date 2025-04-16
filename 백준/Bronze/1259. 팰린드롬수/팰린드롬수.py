while True:
    N = input().strip()
    if N == "0":
        break

    flag = True
    arr = list(N)
    for i in range(int(len(arr) / 2)):
        if arr[i] != arr[-(i + 1)]:
            print("no")
            flag = False
            break
    if flag:
        print("yes")
