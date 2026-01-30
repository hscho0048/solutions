

a = int(input())
i = 0
ok = True

while i < a:

    brackets = input()
    stack = []
    ok = True

    for b in brackets:
        if b == "(":
            stack.append(b)
        
        elif b == ")":
            if not stack:
                ok = False
                break
            
            stack.pop()

    if ok and not stack:
        print('YES')
    
    else: print('NO')
                
    i += 1