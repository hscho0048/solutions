from collections import deque

T = int(input())

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for _ in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    if start_x == end_x and start_y == end_y:
        print(0)
        continue

    visited = [[-1] * l for _ in range(l)]
    queue = deque()

    queue.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            print(visited[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))