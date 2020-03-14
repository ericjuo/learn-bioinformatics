with open('rosalind_grph.txt', 'rt') as fin:
    name = []
    s = ''
    seq = []
    for line in fin:
        line = line.strip('\n')
        if line.startswith(">"):
            if s:
                seq.append(s)
                s = ''
            line = line.strip('>')
            name.append(line)
        else:
            s += line
    seq.append(s)
with open('rosalind_grph_ans.txt', 'wt') as fout:
    for i, s in enumerate(seq):
        for j, t in enumerate(seq):
            if s[-3:] == t[:3] and s != t:
                print(name[i], name[j], file = fout)