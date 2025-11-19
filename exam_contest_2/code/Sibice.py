import math


n, w, h = [int(x) for x in input().split()]
max_len = int(math.sqrt(w ** 2 + h ** 2))

for _ in range(n):
    match = int(input())
    if match > max_len:
        print('NE')
    else:
        print('DA')