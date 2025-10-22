r, c = [int(x) for x in input().split()]
init_x, init_y = [int(x) for x in input().split()]
dest_x,dest_y = [int(x) for x in input().split()]
x, y = init_x - 1, init_y - 1
dest_x -= 1
dest_y -= 1

grid = []

for _ in range(r):
    grid.append([int(x) for x in list(input())])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir = 0

visited = set()

def can_move(nx, ny):
    return 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 0

while True:
    if (x, y) == (dest_x, dest_y):
        print(1)
        break
    state = (x, y, dir)
    if state in visited:
        print(0)
        break
    visited.add(state)
    left_dir = (dir + 3) % 4
    lx, ly = x + dirs[left_dir][0], y + dirs[left_dir][1]
    if can_move(lx, ly):
        dir = left_dir
        x, y = lx, ly
        continue
    fx, fy = x + dirs[dir][0], y + dirs[dir][1]
    if can_move(fx, fy):
        x, y = fx, fy
        continue
    dir = (dir + 1) % 4