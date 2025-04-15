import heapq

N = int(input().strip())
M = int(input().strip())

INF = 1e9


def dajikstra(st, distance, graph):
    pq = []
    heapq.heappush(pq, (0, st))
    distance[st] = 0

    while pq:
        cost, now = heapq.heappop(pq)

        if distance[now] < cost:
            continue

        for next, ncost in graph[now]:
            weight = cost + ncost
            if weight < distance[next]:
                distance[next] = weight
                heapq.heappush(pq, (weight, next))


graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)


for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append([v, c])

st, end = map(int, input().split())

dajikstra(st, distance, graph)

print(distance[end])
