p1 = [int(n) for n in input().split()]
p2 = [int(n) for n in input().split()]
p3 = [int(n) for n in input().split()]
p4 = [int(n) for n in input().split()]
p5 = [int(n) for n in input().split()]

p1 = sum(p1)
p2 = sum(p2)
p3 = sum(p3)
p4 = sum(p4)
p5 = sum(p5)

scores = [p1, p2, p3, p4, p5]

max = p1
max_i = 1
for i in range(1,5):
    if scores[i] > max:
        max = scores[i]
        max_i = i + 1

print(max_i, max)