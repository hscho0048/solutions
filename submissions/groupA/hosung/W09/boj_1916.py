import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

A, B = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_city, cost in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[next_city]:
                distance[next_city] = new_cost
                heapq.heappush(q, (new_cost, next_city))


dijkstra(A)
print(distance[B])