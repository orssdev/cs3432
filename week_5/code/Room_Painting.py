n, m = [int(x) for x in input().split()]

sizes = []

colors = []

for _ in range(n):
    sizes.append(int(input()))

sizes.sort()

for _ in range(m):
    colors.append(int(input()))

# cans = []

# for c in colors:
#     l = []
#     for s in sizes:
#         if c < s:
#             l.append(s)
#             break
#         l.append(s * ((c // 2) + 1))
#     cans.append(l)
        
# cans = list(map(min, cans))


# paint = sum(cans)

# print(paint - sum(colors))

cans = []

index = len(sizes) // 2

for c in colors:
    while sizes[index] > c:
        index = index // 2
    while sizes[index] < c:
        index += 1
    cans.append(sizes[index])

print(sum(cans) - sum(colors))