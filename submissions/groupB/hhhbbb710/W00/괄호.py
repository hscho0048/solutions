import sys

input = sys.stdin.readline

n = int(input())


for i in range(n):
    l = []
    check = True
    st = list(input().strip())
    # print(st)
    for j in range(len(st)):
        if st[0] == '(' : l.append(st.pop(0))
        elif st[0] == ')' :
            if len(l) != 0 : 
                l.pop()
                st.pop(0)
            else :
                check = False
                st.pop(0)
                break
    print("YES") if check and len(l) == 0 else print("NO")