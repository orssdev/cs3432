n = int(input())

az = []
bs = []

for _ in range(n):
  a, b = [int(x) for x in input().split()]
  az.append(a)
  bs.append(b)

a = max(az)
b = min(bs)

if b >= a:
    print('gunilla has a point')
else:
    print('edward is right')