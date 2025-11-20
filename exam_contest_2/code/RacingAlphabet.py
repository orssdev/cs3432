import math

circle = {chr(i + 65): i + 1 for i in range(26)}
circle[' '] = 27
circle["'"] = 28

n = int(input())

for _ in range(n):
    aph = input()

    total_time = 1
    prev = aph[0]

    for ch in aph[1:]:
        diff = abs(circle[ch] - circle[prev])
        step_dist = min(diff, 28 - diff)

        dist_feet = step_dist * (math.pi * 60) / 28
        total_time += dist_feet / 15
        total_time += 1
        prev = ch

    print(f'{total_time:.10f}')


