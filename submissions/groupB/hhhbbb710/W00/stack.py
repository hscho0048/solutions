import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    st = input().split()
    if st[0] == 'push': stack.append(st[1])
    elif st[0] == 'pop' : print(stack.pop(-1)) if len(stack) != 0 else print(-1)
    elif st[0] == 'size' : print(len(stack))
    elif st[0] == 'empty' : print(0) if len(stack) != 0 else print(1)
    elif st[0] == 'top' : print(stack[-1]) if len(stack) != 0 else print(-1)