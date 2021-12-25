def divdigit(n):
    b = []
    k = n
    while n > 0:
        b.append(n % 10)
        n = n // 10
    i = 0
    for elem in b:
        if elem != 0 and k % elem == 0:
            i += 1

    return i
