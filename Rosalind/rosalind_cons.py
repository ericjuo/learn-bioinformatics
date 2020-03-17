with open('./Rosalind/rosalind_cons.txt', 'rt') as fin:
    name = []
    s = ''
    seq = []
    for line in fin:
        line = line.strip('\n')
        if line.startswith('>'):
            if s:
                seq.append(s)
                s = ''
            line = line.strip('>')
            name.append(line)
        else:
            s += line
    seq.append(s)

length = len(seq[0])
a, c, g, t = [0]*length, [0]*length, [0]*length, [0]*length
acgt_dict = {'A': a, 'C': c, 'G': g, 'T': t}
for s in seq:
    for i in range(length):
        if s[i] == 'A':
            a[i] += 1
        elif s[i] == 'C':
            c[i] += 1
        elif s[i] == 'G':
            g[i] += 1
        else:
            t[i] += 1
with open('./Rosalind/rosalind_cons_ans.txt', 'wt') as fout:
    cons = ''
    for a, c, g, t in zip(acgt_dict['A'], acgt_dict['C'], acgt_dict['G'], acgt_dict['T']):
        if max(a, c, g, t) == a:
            cons += 'A'
        elif max(a, c, g, t) == c:
            cons += 'C'
        elif max(a, c, g, t) == g:
            cons += 'G'
        else:
            cons += 'T'
    print(cons, file = fout)
    for key, value in acgt_dict.items():
        value = ' '.join(str(v) for v in value)
        print(f'{key}: {str(value)}', file = fout)

    

    
