n = int(input())

guest = [int(g) for g in input().split()]

indexes = {}
awkwardness_level = n

for i in range(n):
    if guest[i] in indexes:
        diff = i - indexes[guest[i]]
        if diff < awkwardness_level:
            awkwardness_level = diff
    else:
        indexes[guest[i]] = i

print(awkwardness_level)