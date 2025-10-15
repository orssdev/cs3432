import math
import bisect

try:
    while True:
        n, l, w = [int(x) for x in input().split()]
        end_points = []
        for _ in range(n):
            c, r = [int(x) for x in input().split()]
            offset = math.sqrt((r ** 2) - ((w / 2) ** 2))
            end_points.append((c - offset, c + offset))
        end_points.sort()

        left_ends = [p[0] for p in end_points]
        right_ends = [p[1] for p in end_points]

        if min(left_ends) > 0:
            print(-1)
            break

        count = 0
        covered = 0

        while covered < l and count <= n:
            index = bisect.bisect_left(left_ends, covered) - 1
            covered = right_ends[index]
            count += 1
        
        if count <= n and l <= covered:
            print(count)
        else:
            print(-1)
except:
    pass