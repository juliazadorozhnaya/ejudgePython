import itertools


def LookSay():
    number = [1]
    while True:
        for i in number:
            yield i
        new_number = []
        for k, g in itertools.groupby(number):
            new_number.append(len(list(g)))
            new_number.append(k)
        number = new_number

