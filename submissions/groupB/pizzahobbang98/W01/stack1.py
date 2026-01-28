N = int(input("반복 횟수를 입력하세요 : "))

for i in range(N):
    
    s = input("괄호 문자열을 입력하세요 : ")
    s_lst=[]
    sum=0
    for j in s:
        s_lst.append(j)
    
    for k in s_lst:
        if k=='(':
            sum+=1
        elif k==')':
            sum-=1
            if sum<0:
                print('NO')
                break

    if sum==0:
        print('YES')
    elif sum > 0:
        print('NO')


        