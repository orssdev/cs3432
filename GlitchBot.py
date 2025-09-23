dest_x, dest_y = [int(n) for n in input().split()]

n = int(input())

instructions = []
for i in range(n):
    instruction = input()
    instructions.append(instruction)

dirs = ['N', 'E', 'S', 'W']
moves = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}
options = ['Left', 'Right', 'Forward']

for i in range(n):
    for o in options:
        if o == instructions[i]:
            continue

        temp = instructions[:]
        temp[i] = o

        x = 0
        y = 0
        dir_idx = 0

        for ins in temp:
            if ins == 'Left':
                dir_idx = (dir_idx - 1) % 4
            elif ins == 'Right':
                dir_idx = (dir_idx + 1) % 4
            elif ins == 'Forward':
                dx, dy = moves[dirs[dir_idx]]
                x += dx
                y += dy

        if x == dest_x and y == dest_y:
            print(i + 1, o)
            exit()
