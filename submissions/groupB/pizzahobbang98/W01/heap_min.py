import heapq
n = int(input("반복연산 횟수를 입력하세요:"))
heap=[]
for i in range(n):
    
    T = int(input("정수를 입력하세요 : "))
    
    if T != 0:
        heapq.heappush(heap,T)
    
    elif (T==0) & (len(heap) != 0) :

        result=heapq.heappop(heap)
        print(result)
    else:
        print(0)
        