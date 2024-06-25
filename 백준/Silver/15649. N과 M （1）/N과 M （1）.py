n,m = map(int,input().split())

visited = [0 for _ in range(1,n+1)]
ptr = []

#test
# print(visited)

#back tracking funtion
def back():
    # 백트레킹 종료 조건
    if len(ptr) == m:
        print(' '.join(map(str, ptr)))
        return
    #실제 로직
    for i in range(1,n+1):
        if visited[i-1] == False:
            visited[i-1] = True
            ptr.append(i)
            back()
            visited[i-1] = False
            ptr.pop()

back()