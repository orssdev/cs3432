cases = int(input())

def valid_word(D: str, E: str):
    D_abc = set('abcdefghijklmnopqrstuvwxyz')
    E_abc = set('abcdefghijklmnopqrstuvwxyz')
    cipher = {}
    if len(D) != len(E) or len(set(D)) != len(set(E)):
        return (False, {})
    for i in range(len(D)):
        if E[i] not in cipher:
            cipher[E[i]] = D[i]
            D_abc.discard(D[i])
            E_abc.discard(E[i])
        elif cipher[E[i]] != D[i]:
            return (False, {})
    if len(set(D)) == 25:
        cipher[list(E_abc)[0]] = list(D_abc)[0]
    return (True, cipher)    


for _ in range(cases):
    n = int(input())
    E_Words = []
    for _ in range(n):
        E_Words.append(input())
    D_Word = input()
    X_Word = input()
    ciphers = []
    for word in E_Words:
        valid, dict = valid_word(D_Word, word)
        if valid:
            ciphers.append(dict)
    if len(ciphers) != 0:
        result = ''
        for c in X_Word:
            first = ciphers[0].get(c)
            all_same = all(cipher.get(c) == first for cipher in ciphers)
            if all_same and first != None:
                result += first
            else:
                result += '?'
        print(result)
    else:
        print('IMPOSSIBLE')