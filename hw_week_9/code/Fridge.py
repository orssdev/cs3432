from collections import Counter

digits = input()
count = Counter(digits)

for i in '123456789':
    if count[i] == 0:
        print(i)
        exit()

min_value = min(count.values())

for k in count:
    count[k] -= min_value
