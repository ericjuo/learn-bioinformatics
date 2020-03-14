def fasta(x):
    with open(x, 'rt') as fin:
        from collections import defaultdict
        name, seq = None, []
        fas = defaultdict(str)
        for line in fin:
            line = line.strip('\n')
            if line.startswith('>'):
                line = line.strip('>')
                if name: fas[name] = ''.join(seq)
                name, seq = line, []
            else:
                seq.append(line)
        if name: fas[name] = ''.join(seq)
    return fas
with open('stronghold05.txt', 'wt') as fout:
    hGC_name, hGC = None, 0
    for name, seq in fasta('C:\\Users\\User\\Desktop\\Rosalind\\rosalind_gc.txt').items():
        gc = (seq.count('C') + seq.count('G')) / len(seq) * 100
        while gc > hGC:
            hGC_name, hGC = name, gc
    print(hGC_name, file = fout)
    print(hGC, file = fout)


