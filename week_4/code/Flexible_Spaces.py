w, p = [int(n) for n in input().split()]
part = [0] + [int(n) for n in input().split()] + [w]

s = set()

for i in part:
    for j in part:
        if j > i:
            s.add(j - i)

print(' '.join([str(n) for n in sorted(list(s))]))