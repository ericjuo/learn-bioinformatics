with open('C:\\Users\\User\\Desktop\\Rosalind\\rosalind_revc.txt', 'rt') as f:
    s = f.read().upper()
    sc = ''
    for n in s[::-1]:
        if n == 'A':
            sc += 'T'
        elif n == 'T':
            sc += 'A'
        elif n == 'C':
            sc += 'G'
        elif n == 'G':
            sc += 'C'
with open('stronghold03.txt', 'wt') as g:
    print(sc, file = g)