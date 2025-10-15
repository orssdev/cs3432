n = int(input())

prices = [int(x) for x in input().split()]
prices.sort()
prices.reverse()

total = 0

for i in range(0, n - 2, 3):
    total += prices[i + 2]

print(total)