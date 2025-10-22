from collections import Counter

digits = input()
count = Counter(digits)

for i in '123456789':
    if count[i] == 0:
        print(i)
        exit()

min_count = min(count[i] for i in '123456789')

for i in '123456789':
    count[i] -= min_count

smallest_digit = min(d for d in '123456789' if count[d] > 0) if any(count[d] > 0 for d in '123456789') else '1'
print(smallest_digit + '0' * (min_count))