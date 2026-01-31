import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

best = 0
for comb in combinations(cards, 3):
    s = sum(comb)
    if best < s <= m:
        best = s

print(best)