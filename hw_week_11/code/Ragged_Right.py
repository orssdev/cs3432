lines = []
max_len = 0
try:
    while True:
        line = input()
        if len(line) > max_len:
            max_len = len(line)
        lines.append(line)
except:
    pass
scores = []
for line in lines:
    scores.append((len(line) - max_len) ** 2)

print(sum(scores[:-1]))