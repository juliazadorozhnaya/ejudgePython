"""Определитель матрицы 4×4
Матрица 4×4 задаётся кортежем из 4 кортежей по 4 целых числа в каждом.
Написать функцию det4(r0, r1, r2, r3), вычисляющую точный определитель матрицы (r0, r1, r2, r3).
Пользоваться itertools нельзя."""

def det_3(row1, row2, row3):
    return row1[0] * row2[1] * row3[2] + row1[1] * row2[2] * row3[0] \
           + row1[2] * row2[0] * row3[1] - row1[2] * row2[1] * row3[0] \
           - row1[1] * row2[0] * row3[2] - row1[0] * row2[2] * row3[1]


def det4(row1, row2, row3, row4):
    return row1[0] * det_3(row2[1:], row3[1:], row4[1:]) \
           - row2[0] * det_3(row1[1:], row3[1:], row4[1:]) \
           + row3[0] * det_3(row1[1:], row2[1:], row4[1:]) \
           - row4[0] * det_3(row1[1:], row2[1:], row3[1:])

