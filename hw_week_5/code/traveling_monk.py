a, d = [int(x) for x in input().split()]

segments = []
total_time = 0
total_height = 0
for _ in range(a):
    h, t = map(int, input().split())
    speed = h / t if t != 0 else 0
    segments.append((total_time, total_height, t, h, speed))
    total_time += t
    total_height += h

ascent_segments = segments
segments = []
total_time = 0
total_height = 0
for _ in range(d):
    h, t = map(int, input().split())
    speed = h / t if t != 0 else 0
    segments.append((total_time, total_height, t, h, speed))
    total_time += t
    total_height += h

descent_segments = segments

for i in range(len(descent_segments)):
        start_time, _, duration, height, speed = descent_segments[i]
        descent_segments[i] = (start_time, total_height, duration, height, -speed)
        total_height -= height 

left = 0.0
right = total_time
eps = 1e-7

def get_height_at_time(segments, t):
    for start_time, start_height, duration, height, speed in segments:
        end_time = start_time + duration
        if t <= end_time:
            return start_height + (t - start_time) * speed
    return segments[-1][1] + segments[-1][3]


while right - left > eps:
    mid = (left + right) / 2
    h_up = get_height_at_time(ascent_segments, mid)
    h_down = get_height_at_time(descent_segments, mid)

    if h_up < h_down:
        left = mid
    else:
        right = mid
    
print(f"{left:.6f}")
