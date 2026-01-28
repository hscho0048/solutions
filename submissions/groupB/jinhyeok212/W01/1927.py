# 최소 힙

import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    
    if x > 0:
        heapq.heappush(arr, x)
    elif x == 0:
        if arr:
            result = heapq.heappop(arr)
            print(result)
        else:
            print(0)

#heapq.heappush(heap, item) item을 heap에 추가
#heapq.heappop(heap) heap에서 가장 작은 원소를 pop & 리턴. 비어있는 경우 IndexError뜸
#heapq.heapify(x) 리스트 x를 즞각적으로 heap으로 변환함