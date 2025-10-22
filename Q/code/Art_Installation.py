r, g, b = [int(x) for x in input().split()]
cr, cg, cb = [int(x) for x in input().split()]
crg, cgb = [int(x) for x in input().split()]

need = 0

if r > cr:
    diff = (r - cr)

    if diff <= crg:
        need += diff
        crg -= diff
    else:
        print(-1)
        exit()

if b > cb:
    diff = (b - cb)

    if diff <= cgb:
        need += diff
        cgb -= diff
    else:
        print(-1)
        exit()

if g > cg:
    diff = (g - cg)

    if diff <= (crg + cgb):
        need += diff
    else:
        print(-1)
        exit()

print(need)