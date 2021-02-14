# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Probability of getting heterozygotes [Aa], given the mate is heterozygotes [Aa], is 0.5
# Probability of getting double heterozygotes [AaBb] is 0.5 * 0.5 = 0.25
pHeter = 0.25
pHomo = 1 - pHeter
k = 2
n = 1

def accum_binom(k, n):
    population = 2 ** k
    def fractional(a):
        '''Calculate fractional of a positive integer n.
        n! = n * (n-1) * ...* 3 * 2 * 1'''
        product = a
        i = a
        while i > 1:
            product = product * (i - 1)
            i -= 1
        return product
    assert fractional(2) == 2, 'fractional function is not working'
    def combination(b, c):
        '''C(m, k) = m! / k!(m-k)!'''
        if b == c:
            return 1
        return fractional(b) / (fractional(c) * fractional(b - c))
    assert combination(2, 1) == 2, 'combination function is not working'
    def p(pop, d):
        '''Calculate bionominal distribution. Binom = C(m, k) * P**k * (1 - P)**(m - k) '''
        return combination(pop, d) * (0.25**d) * (0.75**(pop - d))
    assert p(2, 1) == 0.375, 'p function is not working'
    return sum([p(population, i) for i in range(n, population + 1)])
report = 'Probability of at least %d AaBb organisms in %dth generation is %.3f' %(n, k, accum_binom(k, n))
print(report)


# %%
