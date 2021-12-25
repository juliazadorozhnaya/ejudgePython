from itertools import islice


def joinseq(*args):
    ind = [0] * len(args)
    while True:
        mn, mni = None, None
        for i in range(len(args)):
            index = ind[i]
            if index >= len(args[i]):
                continue
            el = args[i][index]
            if not mn or el < mn:
                mn, mni = el, i
        if not mn:
            return
        ind[mni] += 1
        yield mn


#print("".join(joinseq("abs", "qr", "azt")))
