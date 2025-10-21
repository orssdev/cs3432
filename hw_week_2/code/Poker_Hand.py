cards = input().split()

count = [0] * 13

for c in cards:
    rank = c[0]
    if rank == 'A':
        count[0] += 1
    elif rank == '2':
        count[1] += 1
    elif rank == '3':
        count[2] += 1
    elif rank == '4':
        count[3] += 1
    elif rank == '5':
        count[4] += 1
    elif rank == '6':
        count[5] += 1
    elif rank == '7':
        count[6] += 1
    elif rank == '8':
        count[7] += 1
    elif rank == '9':
        count[8] += 1
    elif rank == 'T':
        count[9] += 1
    elif rank == 'J':
        count[10] += 1
    elif rank == 'Q':
        count[11] += 1
    elif rank == 'K':
        count[12] += 1

print (max(count))