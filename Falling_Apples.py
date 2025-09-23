row, col = [int(i) for i in input().split()]

grid = [list(input()) for _ in range(row)]

for c in range(col):
    temp = row - 1
    for r in range(row - 1, -1, -1):
        if grid[r][c] == '#':
            temp = r - 1
        elif grid[r][c] == 'a':
            if temp != r:
                grid[temp][c] = 'a'
                grid[r][c] = '.'
            temp -= 1  

for r in grid:
    print(''.join(r))
