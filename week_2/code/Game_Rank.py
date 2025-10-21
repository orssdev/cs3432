matches = input()

con_wins = 0
rank = 25
stars = 0

for m in matches:
    if m == 'W':
        con_wins += 1
        stars += 1
        if con_wins >= 3 and rank >= 6 and rank <= 25:
            stars += 1
        if rank > 20:
            if stars > 1:
                rank -= 1
                stars = stars % 2
        elif rank > 15:
            if stars > 2:
                rank -= 1
                stars = stars % 3
        elif rank > 10:
            if stars > 3:
                rank -= 1
                stars = stars % 4
        elif rank > 0:
            if stars > 4:
                rank -= 1
                stars = stars % 5
    else:
        con_wins = 0
        if rank <= 20:
            if stars > 0:
                stars -= 1
            else:
                if rank != 20:
                    rank += 1
                

    
