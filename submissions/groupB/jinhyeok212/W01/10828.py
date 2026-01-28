# 스택

import sys
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.items:
            print('-1')
        else: 
            print(self.items.pop())

    def size(self):
        return print(len(self.items))
    
    def empty(self):
        if not self.items:
            print('1') 
        else:
            print('0')

    def top(self):
        if not self.items:
            print('-1') 
        else:
            print(self.items[-1])

input = sys.stdin.readline
a = int(input())

s = Stack()

for i in range(a):
    b = input().split()

    if b[0] == 'push':
        s.push(int(b[1]))
    elif b[0] == 'pop':
        s.pop()
    elif b[0] == 'size':
        s.size()
    elif b[0] == 'empty':
        s.empty()
    elif b[0] == 'top':
        s.top()

