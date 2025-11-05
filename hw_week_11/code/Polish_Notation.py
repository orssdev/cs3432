try:
    def is_valid_int(s):
        try:
            int(s)
            return True
        except:
            return False

    def eval_expr(opr: str, op1: str, op2: str):
        if is_valid_int(op1) and is_valid_int(op2):
            result = ''
            if opr == '*':
                result = int(op1) * int(op2)
            elif opr == '+':
                result = int(op1) + int(op2)
            elif opr == '-':
                result = int(op1) - int(op2)
            return(str(result))
        
        return f'{opr} {op1} {op2}'

    case_num = 1
    while True:
        stack = []
        expr: list[str] = input().split()[::-1]
        for c in expr:
            if  c == '*' or c == '+' or c == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                result = eval_expr(c, op1, op2)
                stack.append(result)
            else:
                stack.append(c)
        print(f'Case {case_num}: {" ".join(stack)}')
        case_num += 1
except:
    pass