n, h = [int(x) for x in input().split()]

obstacles = []


for _ in range(n):
    obstacles.append(int(input()))

collisions = {}
occurrences = set()

for level in range(1, h + 1):
    count = 0
    for i in range(n):
        if i % 2 == 0:
            if level <= obstacles[i]:
                count += 1
        else:
            if level > (h - obstacles[i]):
                count += 1
    if count in collisions:
        collisions[count] += 1
    else:
        collisions[count] = 1 
    occurrences.add(count)

min_occur = min(occurrences)

print(min_occur, collisions[min_occur])