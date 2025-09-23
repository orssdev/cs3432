try:
    env = {}
            
    line = input()

    while True:
        tokens = line.split()
        if tokens[0] == 'clear':
            env = {}
        elif tokens[0] == 'def':
            env[tokens[1]] = int(tokens[2])
        elif tokens[0] == 'calc':
            if tokens[1] in env:
                flag = True
                value = env[tokens[1]]
                for i in range(2, len(tokens), 2):
                    if tokens[i] == '+':
                        if tokens[i + 1] in env:
                            value += env[tokens[i + 1]]
                        else:
                            flag = False
                            break
                    elif tokens[i] == '-':
                        if tokens[i + 1] in env:
                            value -= env[tokens[i + 1]]
                        else:
                            flag = False
                            break
                if flag:
                    keys = [key for key, val in env.items() if val == value]
                    if len(keys) == 0:
                        print(' '.join(tokens[1:]), 'unknown')
                    else:
                        print(' '.join(tokens[1:]), f'{keys[0]}')
                else:
                    print(' '.join(tokens[1:]), 'unknown')

            else:
                print(' '.join(tokens[1:]), 'unknown')
        line = input()
except:
    pass
