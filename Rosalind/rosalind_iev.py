com = [('AA', 'AA'), ('AA', 'Aa'), ('AA', 'aa'), ('Aa', 'Aa'), ('Aa', 'aa'), ('aa', 'aa')]
o = []
for i in range(len(com)):
    o.append([])
    for j in range(2):
        for k in range(2):
            x = com[i][0][j] + com[i][1][k]
            o[i].append(x)

pd = []
for i in o:
    counter = 0
    for j in i:
        if 'A' in j:
            counter += 1
    rate = counter / len(i)
    pd.append(rate)

with open('./Rosalind/rosalind_iev.txt', 'rt') as fin:
    nums = [int(n) for n in fin.read().split()]
    print(nums)
with open('./Rosalind/rosalind_iev_ans.txt', 'wt') as fout:
    result = []
    for n, p in zip(nums, pd):
        result.append(n * p * 2)
    fout.write(str(sum(result)))