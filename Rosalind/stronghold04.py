n = 35
k = 4
fb = [1, 1]
for i in range(n):
    if i == 0 or i == 1:
        continue
    fb.append(fb[i-2]*k + fb[i-1])
print(fb[n-1])