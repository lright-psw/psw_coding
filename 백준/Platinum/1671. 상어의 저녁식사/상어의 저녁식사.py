N = int(input())
sharks = [tuple(map(int, input().split())) for _ in range(N)]

adj = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if sharks[i] == sharks[j] and i > j:
            continue
        if all(a >= b for a, b in zip(sharks[i], sharks[j])):
            adj[i].append(j)

match = [-1] * N


def dfs(x, visited):
    for y in adj[x]:
        if visited[y]:
            continue
        visited[y] = True
        if match[y] == -1 or dfs(match[y], visited):
            match[y] = x
            return True
    return False


result = 0
for i in range(N):
    for _ in range(2):
        visited = [False] * N
        if dfs(i, visited):
            result += 1

print(N - result)