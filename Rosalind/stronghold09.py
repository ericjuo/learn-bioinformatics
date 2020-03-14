#n = 81
#m = 19
#result = [1,1]
#for i in range(2, n):
#    x = result[i-1] + result[i-2]
#    if i == m:
#        x -= 1
#    elif i > m:
#        x -= result[i-m-1]
#    result.append(x)
#print(result[-1])
#f = [1] * 100
#print(f)
#for i in range(6):
#    print(i)

ages = [1] + [0]*(3-1)
for i in range(10 - 1):
 ages = [sum(ages[1:])] + ages[:-1]
print(sum(ages))

