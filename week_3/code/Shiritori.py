n = int(input())
player = 1

words = []
for i in range(n):
    words.append(input())

for i in range(n - 1):
    word = words[i]
    if words[i][len(word) - 1] != words[i + 1][0] or word in words[:i]:
        player = ((i + 1) % 2) + 1 
        if word in words[:i]:
             player = (i % 2) + 1 
        print(f'Player {player} lost')
        exit()
if words[len(words) - 1] in words[:len(words) - 1]:
        player = ((len(words) + 1) % 2) + 1 
        print(f'Player {player} lost')
        exit()
print('Fair Game')