from itertools import combinations

n, m = [int(x) for x in input().split()]

comb = combinations(range(1, n + 1), 2)

for i in comb:
    print(i)