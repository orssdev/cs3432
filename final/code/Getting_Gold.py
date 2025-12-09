from collections import deque

w, h = [int(x) for x in input().split()]
grid = []
for _ in range(h):
    grid.append(input().strip())

for i in range(h):
    for j in range(w):
        if grid[i][j] == 'P':
            start_r, start_c = i, j
            break

def trap(r, c):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 'T':
            return True
    return False

visited = set()
queue = deque([(start_r, start_c)])
visited.add((start_r, start_c))
gold = 0

if grid[start_r][start_c] == 'G':
    gold += 1

while queue:
    r, c = queue.popleft()
    
    if trap(r, c):
        continue
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and (nr, nc) not in visited:
            if grid[nr][nc] != '#' and grid[nr][nc] != 'T':
                visited.add((nr, nc))
                queue.append((nr, nc))
                if grid[nr][nc] == 'G':
                    gold += 1

print(gold)
