n = int(input())
ai = list(map(int,input().split()))
s = int(input())
cnt = 0

visited = [0 for _ in range(len(ai))]

def dfs(i):
    tmp = i-1
    if visited[tmp] == 0:
        jump = ai[tmp]
        visited[tmp] = 1
        if tmp + jump < len(ai) :
            now = i + jump
            dfs(now)
        if tmp - jump >= 0:
            now = i - jump
            dfs(now)
    else:
        return
    

dfs(s)
for i in visited:
    if i == 1:
        cnt+=1

print(cnt)