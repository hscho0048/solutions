num = int(input())

output = []
for _ in range(num) :

    cnt_front = 0
    cnt_back = 0

    ps_str = input()
    ps = list(ps_str)

    for i in ps :
        if i == "(" :
            cnt_front += 1
        elif i == ")" :
            cnt_back += 1

        if cnt_back > cnt_front :
            break
        
    if cnt_front == cnt_back :
        output.append("YES")
    else :
        output.append("NO")

print('\n'.join(output))