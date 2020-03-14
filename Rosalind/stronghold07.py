def dominate(k, m , n):
    from collections import defaultdict
    ls = {'k': k, 'm': m, 'n': n}
    total = k + m + n
    p1 = {p: q / total for p, q in ls.items()}
    p2 = defaultdict()
    for i in p1:
        for j in p1:
            if i == j:
                p2[i+j] = p1[i] * (p1[j]*total - 1) / (total -1)
            else: 
                p2[i+j] = p1[i] * (p1[j]*total) / (total -1)
    prec = p2['nn'] + (p2['nm'] + p2['mn']) * 0.5 + p2['mm'] * 0.25
    print(1 - prec)
dominate(18, 21, 28)
            

