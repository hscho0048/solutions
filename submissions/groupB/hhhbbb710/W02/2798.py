from itertools import combinations
import sys

input = sys.stdin.readline

st = input().split()
M = int(st[1])

st = list(map(int, input().split()))  # 받은 값을 int로 바꾸고 리스트에 저장
result = list(combinations(st, 3))  # 받은 문자열을 3개씩 조합으로 묶어 리스트에 반환

sum_list = []
for i in result:  # 조합 중 M보다 작거나 같은수만 sum_list에 추가
    if sum(i) <= M:
        sum_list.append(sum(i))
print(max(sum_list))  # sum_list중 가장 큰 값 출력