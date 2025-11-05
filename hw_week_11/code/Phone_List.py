test_cases = int(input())

def check(numbers: list[str]):
    numbers.sort(key=len)
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(i + 1, len_numbers):
            if numbers[i] == numbers[j][:len(numbers[i])]:
                return True
    return False



for _ in range(test_cases):
    numbers_list = {
        '0': [],
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': []
    }
    n = int(input())

    for _ in range(n):
        number = input()
        numbers_list[number[0]].append(number)
    count = 0
    for numbers in numbers_list.values():
        if len(numbers) > 1 and check(numbers):
            print('NO')
            break
        count += 1
    
    if count == len(numbers_list):
        print('YES')