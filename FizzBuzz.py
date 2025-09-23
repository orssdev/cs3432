x, y, n = input().split()

for i in range(1, int(n) + 1):
    ix = int(i) % int(x)
    iy = int(i) % int(y)

    if not ix and not iy:
        print('FizzBuzz')
    elif not ix:
        print('Fizz')
    elif not iy:
        print('Buzz')
    else:
        print(i)