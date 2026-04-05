from collections import deque

N, K = map(int, input().split())

MAX = 100000
visited = [-1] * (MAX + 1)

queue = deque()
queue.append(N)
visited[N] = 0

while queue:
    now = queue.popleft()

    if now == K:
        print(visited[now])
        break

    for next_pos in (now - 1, now + 1, now * 2):
        if 0 <= next_pos <= MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[now] + 1
            queue.append(next_pos)