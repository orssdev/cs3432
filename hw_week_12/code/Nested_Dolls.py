t = int(input())

for _ in range(t):
    m = int(input())
    nums = [int(x) for x in input().split()]
    dolls = []
    for i in range(0, len(nums), 2):
        dolls.append((nums[i], nums[i + 1]))
    dolls.sort()
    print(dolls)
    count = 1
    prev_doll_h = 0
    for doll in dolls:
        doll_h = doll[1]
        if doll_h <= prev_doll_h:
            count += 1
        prev_doll_h = doll_h
    print(count)