vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

chars = input()
len_chars = len(chars)

blanks = [i for i in range(len(chars)) if chars[i] == '_']


if len_chars < 3:
    if 'L' in chars:
        print(len(blanks) * 26)
    else:
        if len(blanks) == 2:
            print(51)
        else:
            print(1)
else:
    count = 0
    if 'L' in chars:
        for i in blanks:
            if i == 0 and (i + 1 not in blanks) and (i + 2 not in blanks):
                pass
            elif i == len_chars - 1:
                pass
            else:
                pass
    else:
        pass