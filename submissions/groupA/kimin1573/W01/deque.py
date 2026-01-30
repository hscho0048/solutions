
num = int(input())
i = 0
deque = []
output = []

while i < num:

    input_func = input()

    if input_func.split()[0] == 'push_front':
        deque.insert(0, input_func.split()[1])
        i += 1

    elif input_func.split()[0] == 'push_back': 
        deque.append(input_func.split()[1])
        i += 1 

    elif input_func == 'pop_front':
        output.append(deque.pop(0)if deque else '-1')
        i += 1

    elif input_func == 'pop_back':  
        output.append(deque.pop()if deque else '-1')
        i += 1

    elif input_func == 'size':
        output.append(str(len(deque)))
        i += 1

    elif input_func == 'empty':
        output.append('1' if len(deque) == 0 else '0')
        i += 1

    elif input_func == 'front':
        output.append('-1' if len(deque) == 0 else deque[0])
        i += 1

    elif input_func == 'back':
        output.append('-1' if len(deque) == 0 else deque[-1])
        i += 1

print('\n' .join(output))