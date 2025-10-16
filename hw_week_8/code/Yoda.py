n = [int(x) for x in list(input())]
m = [int(x) for x in list(input())]


result_n = []
result_m = []

nl = len(n)
ml = len(m)

if nl > ml:
    m = ([0] * (nl - ml)) + m
elif ml > nl:
    n = ([0] * (ml - nl)) + n

for i in range(max(nl, ml)):
    ni = n[i] 
    mi = m[i] 
    if ni > mi:
        result_n.append(ni)
    elif mi > ni:
        result_m.append(mi)
    else:
        result_n.append(ni)
        result_m.append(mi)
        
if len(result_n) != 0:
    print(int(''.join([str(x) for x in result_n])))
else:
    print('YODA')

if len(result_m) != 0:
    print(int(''.join([str(x) for x in result_m])))
else:
    print('YODA')