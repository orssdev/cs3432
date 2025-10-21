GSC = input().split()

buying_power = (int(GSC[0]) * 3) + (int(GSC[1]) * 2) + (int(GSC[2]) * 1)

victory = ''

if buying_power >= 8:
    victory = 'Province'
elif buying_power >= 5:
    victory = 'Duchy'
elif buying_power >= 2:
    victory = 'Estate'

treasure = 'Copper'

if buying_power >= 6:
    treasure = 'Gold'
elif buying_power >= 3:
    treasure = 'Silver'

if victory != '':
    print (f'{victory} or {treasure}')
else:
    print (treasure)