


num = int(input())

i = 0
l = []

while i < num:
    func_input = input()

    if func_input.split()[0] == 'push':
        l.append(int(func_input.split()[1]))
        i += 1
        
    elif func_input == 'top':
        if len(l) == 0:
            print(-1)
            i += 1

        else:
            print(l[-1])
            i += 1
    
    elif func_input == 'pop':
        if len(l) == 0:
            print(-1)
            i += 1
        else:
            print(l[-1])
            del l[-1]
            i += 1

    elif func_input == 'size':

        print(len(l))
        i += 1

    elif func_input == 'empty':
        if len(l) == 0:
            print(1)
            i += 1
        
        else:
            print(0)
            i += 1
    elif func_input == 'top':

        if l:
            print(l[-1])
        
        else: print(-1)
        