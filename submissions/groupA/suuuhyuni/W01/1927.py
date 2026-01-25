import sys
import heapq

input = sys.stdin.readline

num = int(input())

heap = []
output= []
cnt = 0

for _ in range(num) :

    x = int(input())

    if x == 0:
        if heap :
            output.append(heapq.heappop(heap))
        else :
            output.append(0)
    else :
        heapq.heappush(heap, x)
        
print('\n'.join(map(str, output)))