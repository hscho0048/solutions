import sys

input = sys.stdin.readline

n = int(input())
d = []

for i in range(n):
    st = input().split()
    if st[0] == 'push_front': d.insert(0, st[1])
    elif st[0] == 'push_back': d.append(st[1])
    elif st[0] == 'pop_front' : print(d.pop(0)) if len(d) != 0 else print(-1)
    elif st[0] == 'pop_back' : print(d.pop()) if len(d) != 0 else print(-1)
    elif st[0] == 'size' : print(len(d))
    elif st[0] == 'empty' : print(0) if len(d) != 0 else print(1)
    elif st[0] == 'front' : print(d[0]) if len(d) != 0 else print(-1)
    elif st[0] == 'back' : print(d[-1]) if len(d) != 0 else print(-1)