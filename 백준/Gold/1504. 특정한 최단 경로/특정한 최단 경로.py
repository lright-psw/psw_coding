import heapq

INF = 1e9
N, E = map(int, input().split())


def dajikstra(st, graph):
    distance = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, st))
    distance[st] = 0

    while pq:
        cost, now = heapq.heappop(pq)

        if distance[now] > cost:
            continue

        for next, weight in graph[now]:
            next_cost = weight + cost
            if next_cost < distance[next]:
                distance[next] = next_cost
                heapq.heappush(pq, (next_cost, next))
    return distance


graph = [[] for _ in range(N + 1)]


for _ in range(E):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))


v1, v2 = map(int, input().split())

first_dist = dajikstra(1, graph)
v1_dist = dajikstra(v1, graph)
v2_dist = dajikstra(v2, graph)

a = first_dist[v1] + v1_dist[v2] + v2_dist[N]
b = first_dist[v2] + v2_dist[v1] + v1_dist[N]

rst = min(a, b)

print(rst if rst < INF else -1)
