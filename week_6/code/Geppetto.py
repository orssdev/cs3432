n, m = map(int, input().split())
prohibitions = []
for _ in range(m):
    p = list(map(int, input().split()))
    mask = sum(1 << (x-1) for x in p)
    prohibitions.append(mask)

pizzas = 0
for s in range(1 << n):
    if all((s & p) != p for p in prohibitions):
        pizzas += 1

print(pizzas)