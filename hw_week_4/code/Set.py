cards = []

for _ in range(4):
    cards += input().split()

sets = []

def isSet(c1, c2, c3):
    c1_sym = c1[0]
    c2_sym = c2[0]
    c3_sym = c3[0]
    c1_shape = c1[1]
    c2_shape = c2[1]
    c3_shape = c3[1]
    c1_fill = c1[2]
    c2_fill = c2[2]
    c3_fill = c3[2]
    c1_color = c1[3]
    c2_color = c2[3]
    c3_color = c3[3]

    match_sym = (c1_sym == c2_sym) and (c1_sym == c3_sym) and (c2_sym == c3_sym)
    not_match_sym = (c1_sym != c2_sym) and (c1_sym != c3_sym) and (c2_sym != c3_sym)
    match_shape = (c1_shape == c2_shape) and (c1_shape == c3_shape) and (c2_shape == c3_shape)
    not_match_shape = (c1_shape != c2_shape) and (c1_shape != c3_shape) and (c2_shape != c3_shape)
    match_fill = (c1_fill == c2_fill) and (c1_fill == c3_fill) and (c2_fill == c3_fill)
    not_match_fill = (c1_fill != c2_fill) and (c1_fill != c3_fill) and (c2_fill != c3_fill)
    match_color = (c1_color == c2_color) and (c1_color == c3_color) and (c2_color == c3_color)
    not_match_color = (c1_color != c2_color) and (c1_color != c3_color) and (c2_color != c3_color)

    return ((match_sym or not_match_sym) and (match_shape or not_match_shape) and (match_fill or not_match_fill) and (match_color or not_match_color))

for i in range(10):
    for j in range(i + 1, 12):
        for k in range(j + 1, 12):
            card1 = cards[i]
            card2 = cards[j]
            card3 = cards[k]
            if isSet(card1, card2, card3):
                sets.append([i + 1, j + 1, k + 1])

if len(sets) != 0:
    for s in sets:
        print(s[0], s[1], s[2])
else:
    print('no sets')