n = int(input())

proven = set()

for i in range(n):
    expr = input().split('->')
    assumptions = expr[0].split()
    conclusion = expr[1]

    if all(a in proven for a in assumptions):
        proven.add(conclusion)
    else:
        print(i + 1)
        break
else:
    print('correct')
