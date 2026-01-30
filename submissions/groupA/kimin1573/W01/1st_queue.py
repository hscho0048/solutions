num = int(input())
i = 0
l = []
out = []

while i < num:
    cmd = input()

    if cmd.split()[0] == 'push':
        l.append(cmd.split()[1])
        i += 1

    elif cmd == 'pop':
        if len(l) == 0:
            out.append('-1')
        
        else: 
            out.append(l.pop(0))

        i += 1

    elif cmd == 'size':
        out.append(str(len(l)))

        i += 1

    elif cmd == 'empty':
        out.append('1' if len(l) == 0 else '0')

        i += 1

    elif cmd == 'front':
        out.append(l[0] if len(l) != 0 else '-1')
        i += 1

    elif cmd == 'back':
        out.append(l[-1] if len(l) != 0 else '-1')
        i += 1
        
print('\n'.join(out))