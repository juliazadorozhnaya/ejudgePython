"""
Написать функцию checkcomm(fun, *args), которой передаётся не менее одного параметра. Параметр fun — это некоторая n-местная функция,
где n — это длина args. checkcomm() должна возвращать True, если функция fun() на заданных параметрах коммутативна,
то есть в каком бы порядке они ей не передавались, результат одинаков, и False в противном случае. Гарантируется,
что во всех случаях функция вычислима.
"""


def checkcomm(fun, *args):
    result1 = fun(*args)
    result2 = fun(*reversed(args))

    return result1 == result2
