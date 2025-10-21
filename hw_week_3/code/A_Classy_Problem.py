def class_to_num(cls):
    if cls == 'upper':
        return 3
    elif cls =='middle':
        return 2
    else:
        return 1

cases = int(input())
for c in range(cases):
    env = {}
    n = int(input())
    max_depth = 0
    for i in range(n):
        data = input().split()
        name = data[0][:-1]
        rank = [class_to_num(c) for c in data[1].split('-')[::-1]]
        env[name] = rank
        max_depth = max(max_depth, len(rank))
    
    for name in env:
        env[name] = [2] * (max_depth - len(env[name])) + env[name]

    sorted_people = sorted(env.items(), key=lambda item: (item[1], item[0]), reverse=True)

    for person in sorted_people:
        print(person[0])


    print(''.join(['='] * 30))