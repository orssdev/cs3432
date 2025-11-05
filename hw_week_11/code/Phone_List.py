test_cases = int(input())

for _ in range(test_cases):
    sets = {
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set(),
        9: set(),
        10: set()
    }
    n = int(input())
    numbers = []
    numbers_len = set()
    for _ in range(n):
        number = input()
        numbers.append(number)
        numbers_len.add(len(number))
    numbers.sort(key=len)
    Done = False
    for number in numbers:
        for i in numbers_len:
            if i <= len(number):
                num = number[:i]
                if num in sets[i]:
                    print('NO')
                    Done = True
                    break
                if num == number:
                    sets[i].add(num)
        if Done:
            break
    if not Done:
        print('YES')
                