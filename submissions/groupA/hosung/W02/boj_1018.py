import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(sys.stdin.readline().strip())

ans = 64

for a in range(N - 7):
    for b in range(M - 7):
        index1 = 0
        index2 = 0

        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1

        ans = min(ans, index1, index2)

print(ans)
