"""
Написать генератор-функцию PiGen(), которая будет возвращать односимвольные строки — знаки числа Пи (включая 3 и точку).
Первая тысяча таких знаков должна быть точной. Дополнительные требования: Нельзя заранее задавать в виде константы само
число Пи (по ссылке оно есть ☺) или иные данные с точностью более 20 знаков Нельзя вычислять всю тысячу знаков заранее,
а потом выдавать их — не пройдут тесты по времени
"""


def PiGen():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    decimal_point_printed = False

    while True:
        if 4 * q + r - t < n * t:
            yield str(n)
            if not decimal_point_printed and n == 3:
                yield "."
                decimal_point_printed = True
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


