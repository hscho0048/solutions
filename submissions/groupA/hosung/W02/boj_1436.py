import sys

N = int(sys.stdin.readline().split()[0])

cnt = 0
num = 666

while True:
    str_num = str(num)
    if "666" in str_num:
        cnt += 1

    if cnt == N:
        print(num)
        break

    num += 1
