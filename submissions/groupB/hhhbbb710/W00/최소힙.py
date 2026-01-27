import sys
import heapq  # 힙에 빼고 넣고 하기 위한 모듈

input = sys.stdin.readline

n = int(input())
h = []


for i in range(n):
    num = int(input())
    if num == 0:
        if len(h) == 0: print(0)
        else: print(heapq.heappop(h))
    else:
        heapq.heappush(h, num)