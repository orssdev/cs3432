t = int(input())

for _ in range(t):
    n = int(input())
    print((8 * pow(9, n - 1, 1000000007)) % 1000000007)
