m, n = eval(input())

a = [0] * n
for i in range(n):
    a[i] = [0] * m

i = 0
k = 0
p = 0

while i < n * m:
    k = k + 1
    for j in range(k - 1, m - k + 1):
        a[k - 1][j] = (p) % 10
        p = p + 1
        i = i + 1

    if i < n * m:
        for j in range(k, n - k + 1):
            a[j][m - k] = (p) % 10
            p = p + 1
            i = i + 1

    if i < n * m:
        for j in range(m - k - 1, k - 2, -1):
            a[n - k][j] = (p) % 10
            p = p + 1
            i = i + 1

    if i < n * m:
        for j in range(n - k - 1, k - 1, -1):
            a[j][k - 1] = (p) % 10
            p = p + 1
            i = i + 1

for q in range(0, n):
    for w in range(0, m):
        print(a[q][w], end=' ')
    print()