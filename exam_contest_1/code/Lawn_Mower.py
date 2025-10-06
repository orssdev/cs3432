try:
    def merge_intervals(intervals):
        intervals.sort()
        merged = [intervals[0]]
        for cur_start, cur_end in intervals[1:]:
            last_start, last_end = merged[-1]

            if cur_start <= last_end:
                merged[-1] = (last_start, max(last_end, cur_end))
            else:
                merged.append((cur_start, cur_end))
        return merged
    

    def covered(intervals, field_dimention):
        merged = merge_intervals(intervals)
        eps = 1e-6
        if merged[0][0] > 0.0 + eps:
            return False
        for i in range(1, len(merged)):
            if merged[i][0] > merged[i-1][1] + eps:
                return False
        if merged[-1][1] < field_dimention - eps:
            return False
        return True
    

    while True:
        inp = input().split()
        nx = int(inp[0])
        ny = int(inp[1])
        w = float(inp[2])
        length = [float(x) for x in input().split()]
        width = [float(x) for x in input().split()]

        length_intervals = [(x - w/2, x + w/2) for x in length]
        width_intervals = [(y - w/2, y + w/2) for y in width]

        if covered(length_intervals, 75.0) and covered(width_intervals, 100.0):
            print("YES")
        else:
            print("NO")
except:
    pass