from collections import defaultdict

n = int(input())
balloons = [int(x) for x in input().split()]

arrows = defaultdict(int)
shots = 0

for h in balloons:
    if arrows[h] > 0:
        arrows[h] -= 1
        arrows[h - 1] += 1
    else:
        shots += 1
        arrows[h - 1] += 1

print(shots)