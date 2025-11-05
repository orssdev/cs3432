test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input())
    for i, number in enumerate(numbers):
        for num in numbers[i + 1:]:
            if len(number) <= len(num):
                ...
    print(numbers)