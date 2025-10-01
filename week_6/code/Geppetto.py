from itertools import combinations

n, m = [int(x) for x in input().split()]
comb = [()]
for i in range(1, n + 1):
    comb += list(combinations(range(1, n + 1), i))

for _ in range(m):
    prohibition = tuple([int(x) for x in input().split()])
    comb = list(filter(lambda c: not all(x in c for x in prohibition), comb))

print(len(comb))