n, k = [int(x) for x in input().split()]

ns = set()

for _ in range(n):
    ns.add(int(input()))

len_ns = len(ns)

if len_ns > k:
    print(k)
else:
    print(len(ns))