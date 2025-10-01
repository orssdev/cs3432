from itertools import permutations
from datetime import datetime
import heapq

def is_valid_date(s):
    try:
        d = datetime.strptime(s, "%d %m %Y")
        bash_birthday = datetime.strptime('01 01 2000', "%d %m %Y")
        return d >= bash_birthday
    except ValueError:
        return False

t = int(input())
for _ in range(t):
    date = input().split()
    digits = []
    for d in date:
        digits += list(d)
    perm = set(permutations(digits))
    count = 0
    heap = []
    for p in perm:
        s = f'{p[0]}{p[1]} {p[2]}{p[3]} {p[4]}{p[5]}{p[6]}{p[7]}'
        if is_valid_date(s):
            count += 1
            d = datetime.strptime(s, "%d %m %Y")
            heapq.heappush(heap, (d, s))
    if count > 0:
        print(count, heap[0][1])
    else:
        print(0)