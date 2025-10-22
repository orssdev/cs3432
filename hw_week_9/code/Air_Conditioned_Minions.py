n = int(input())

intervals = []

for _ in range(n):
    l, u = [int(x) for x in input().split()]
    intervals.append((u, l))

intervals.sort()

temp = intervals[0][0]
count = 1

for t in intervals[1:]:
    if not (temp <= t[0] and temp >= t[1]):
        temp = t[0]
        count += 1

print(count)