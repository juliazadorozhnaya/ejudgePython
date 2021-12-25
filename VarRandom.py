from random import randint


def randomes(seq):
    result = []
    for s in seq:
        result.append([i for i in s])
        yield randint(result[-1][0], result[-1][1])
    while True:
        for start, end in result:
            yield randint(start, end)
