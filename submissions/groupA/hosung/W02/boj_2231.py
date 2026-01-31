import sys
n = int(sys.stdin.readline().strip())
k = len(str(n))

start = max(1, n - 9*k)

ans = 0
for m in range(start, n):
    s = m + sum(map(int, str(m)))
    if s == n:
        ans = m
        break
print(ans)