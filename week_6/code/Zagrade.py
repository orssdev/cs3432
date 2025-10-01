from itertools import combinations
expr = input()

stack = []
brackets = []

# Find all pairs of brackets
for i, c in enumerate(expr):
    if c == '(':
        stack.append(i)
    elif c == ')':
        index = stack.pop()
        brackets.append((index, i))

results = set()

for r in range(1, len(brackets) + 1):
    for combo in combinations(brackets, r):
        to_remove = set()
        for open_pra, close_pra in combo:
            to_remove.add(open_pra)
            to_remove.add(close_pra)

        new_expr = ''.join(
            ch for i, ch in enumerate(expr) if i not in to_remove
        )
        results.add(new_expr)
for r in sorted(results):
    print(r)