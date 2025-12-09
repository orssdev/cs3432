import math

t = int(input())
for _ in range(t):
    s, n = [int(x) for x in input().split()]
    hatches = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        hatches.append((x, y))
    
    found = False
    for x in range(s + 1):
        for y in range(s + 1):
            if (x, y) in hatches:
                continue
            
            max_hatch_dist = 0
            for hx, hy in hatches:
                dist = math.sqrt((x - hx) ** 2 + (y - hy) ** 2)
                max_hatch_dist = max(max_hatch_dist, dist)
            
            min_edge_dist = min(x, y, s - x, s - y)
            
            if max_hatch_dist <= min_edge_dist:
                print(x, y)
                found = True
                break
        if found:
            break
    
    if not found:
        print("poodle")
