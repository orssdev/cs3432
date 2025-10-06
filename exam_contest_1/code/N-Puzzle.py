correct = {
    'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3),
    'E': (1, 0), 'F': (1, 1), 'G': (1, 2), 'H': (1, 3),
    'I': (2, 0), 'J': (2, 1), 'K': (2, 2), 'L': (2, 3),
    'M': (3, 0), 'N': (3, 1), 'O': (3, 2)
}

grid = [input() for _ in range(4)]

scatter = 0

for r in range(4):
    for c in range(4):
        letter = grid[r][c]
        if letter != '.':
            correct_row, correct_col = correct[letter]
            distance = abs(r - correct_row) + abs(c - correct_col)
            scatter += distance

print(scatter)