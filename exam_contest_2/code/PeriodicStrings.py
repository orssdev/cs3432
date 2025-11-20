def prev(s):
    return s[-1] + s[:-1]

s = input().strip()
n = len(s)

for k in range(1, n + 1):
    if n % k != 0:
        continue
    substring = [s[i:i + k] for i in range(0, n, k)]
    flag = True
    for i in range(1, len(substring)):
        if substring[i] != prev(substring[i-1]):
            flag = False
            break
    if flag:
        print(k)
        break