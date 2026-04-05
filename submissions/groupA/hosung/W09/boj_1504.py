import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    return distance


dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

case1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
case2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

answer = min(case1, case2)

if answer >= INF:
    print(-1)
else:
    print(answer)