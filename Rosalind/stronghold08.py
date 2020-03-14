from collections import defaultdict
with open('rna_code.txt', 'rt') as infile:
#    codeL = infile.read().split()
#    code = dict(zip(codeL[0::2], codeL[1::2]))
    code = {}
    for line in infile:
        for i in range(len(line)):
            if i % 11 == 0:
                code[line[i:i+3]] = line[i+4:i+11].strip()
    

with open('rosalind_prot.txt', 'rt', encoding='utf-8') as fin:
    content = ''
    for line in fin:
        content += line
    rseq = [content[n:n+3] for n in range(len(content)) if n % 3 == 0]
    aaseq = ''
    for r in rseq:
        if code[r] == 'Stop':
            break
        aaseq += code[r]
with open('stronghold08.txt', 'wt') as fout:
    fout.write(aaseq)
    
