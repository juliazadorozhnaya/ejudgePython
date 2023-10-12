"""Написать функцию divrandom(a, b, s, p), принимающую четыре целых ненулевых параметра.
Функция должна возвращать случайно выбранное целое число, не кратное p, из диапазона от a до b
(включительно; таким образом диапазоны a…b и b…a одинаковы) с шагом s. Если такое число выбрать невозможно, функция возвращает 0."""

import random


def divrandom(a, b, s, p):

    if a > b:
        b, a = a, b

    if p == 1:
        return 0

    res = None
    while res is None:
        res = random.randrange(a, b+1, s)

        if res % p == 0:
            res = None

    return res