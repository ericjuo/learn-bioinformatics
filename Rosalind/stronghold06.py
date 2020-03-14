with open('rosalind_hamm.txt', 'rt') as fin:
    s = fin.readline()
    t = fin.readline()
    num = 0
    for i, j in zip(s, t):
        if i != j:
            num += 1
with open('stronghold06.txt', 'wt') as fout:
    print(num, file = fout)
