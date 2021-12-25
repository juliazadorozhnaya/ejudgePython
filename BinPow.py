def BinPow(a, n, f):
    if n == 1:
        return a
    if n % 2 == 1:
        return f(a, BinPow(a, n - 1, f))
    arg = BinPow(a, n/2, f)
    return f(arg, arg)