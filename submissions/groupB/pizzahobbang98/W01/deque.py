import sys
from collections import deque

n= int(input("반복 수행할 정수를 입력하세요: "))

Deque = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push_front':
        Deque.appendleft(command[1])
    
    elif command[0] == 'push_back':
        Deque.append(command[1])
    
    elif command[0] == 'pop_front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
            Deque.popleft()
    
    elif command[0] == 'pop_back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])
            Deque.pop()
    
    elif command[0] == 'size':
        print(len(Deque))
    
    elif command[0] == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    
    elif command[0] =='back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])
        
        
