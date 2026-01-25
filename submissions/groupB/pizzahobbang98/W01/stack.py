import sys
n=int(input("반복 수행할 정수를 입력하세요 :"))
stack=[]

for i in range(n):
    command = sys.stdin.readline().split()

    # push 입력시 스택에 값 추가
    if command[0] == 'push':
        stack.append(command[1])
    
    # pop 입력시 스택 맨 위 값 출력하고 제거 stack의 원소가 아무것도 없을때는 -1 출력
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    
    # size 입력시 스택의 원소 개수 출력
    elif command[0] == 'size':
        print(len(stack))
    
    # empty 입력시 스택이 비어있으면 1 아니면 0 출력
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        
        else:
            print(0)
    
    # top 입력시 스택의 가장 위에 있는 정수 출력
    # 스택에 정수 없는 경우 -1 출력
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        
        else:
            print(stack[-1])
        
            
            