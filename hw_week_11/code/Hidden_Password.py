pw, string = input().split()
pw_chars = list(pw)[::-1]
result = ''
for c in string:
    if c in pw_chars:
        result += c
        pw_chars.pop()
    if result == pw:
        print('PASS')
        exit()

print("FAIL")