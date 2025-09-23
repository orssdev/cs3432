moves = input()

position = 1

for m in moves:
    if m == 'A':
        if position == 1:
            position = 2
        elif position == 2:
            position = 1
    elif m == 'B':
        if position == 2:
            position = 3
        elif position == 3:
            position = 2
    elif m == 'C':
        if position == 1:
            position = 3
        elif position == 3:
            position = 1

print(position)