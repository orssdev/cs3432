n = int(input())

for i in range(n):
    a, b, c = [int(num) for num in input().split()]

    if a + b == c or abs(a - b) == c or a * b == c or a / b == c or b / a == c:
        print('Possible')
    else:
        print('Impossible')