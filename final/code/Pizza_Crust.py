import math


r, c = [int(x) for x in input().split()]

total_area = math.pi * (r ** 2)
cheese_area = math.pi * ((r - c) ** 2)
print(f'{(cheese_area / total_area) * 100:.6f}')