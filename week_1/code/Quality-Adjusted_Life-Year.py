qaly = 0

n = int(input())

for i in range(n):
    q, y = input().split()
    qaly += float(q) * float(y)

print(f'{qaly:.3f}')