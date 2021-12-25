from math import *

def superposition(funmod, funseq):
    res = []
    for i in funseq:
        def func(n, j=i):
            return funmod(j(n))

        res.append(func)
        print()
    return res