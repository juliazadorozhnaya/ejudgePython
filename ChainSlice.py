from itertools import chain, islice


def chainslice(begin, end, *args):
    conc_chain = chain(*args)
    return islice(conc_chain, begin, end)

#print(*(chainslice(17, 33, range(7),  range(8),  range(6),  range(9),  range(5))))
