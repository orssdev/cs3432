s, c, k = [int(x) for x in input().split()]
socks = [int(x) for x in input().split()]
socks.sort()

count = 1
collected = 1
last_sock = socks[0]

for sock in socks[1:]:
    if not ((sock - last_sock) <= k):
        count += 1
        collected = 1
    else:
        collected += 1
        if collected > c:
            count += 1
            collected = 1
    
    last_sock = sock

print(count)