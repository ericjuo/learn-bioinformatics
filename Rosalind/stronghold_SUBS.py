with open('rosalind_subs.txt', 'rt') as fin:
    s, t = fin.read().split()
with open('rosalind_subs_ans.txt', 'wt') as fout:
    location = []
    i = 0
    while t in s[i:]:
        loc = s[i:].find(t)
        i += loc + 1
        location.append(str(i))
    x = ' '.join(location)
    fout.write(x)


