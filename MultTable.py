"""
Ввести два натуральных числа через запятую: N и M. Вывести таблицу умножения от 1 до N включительно в формате,
представленном ниже, разделяя колонки, если они есть, тремя символами «.|.» («.*.» и «.=.» также занимают по три символа).
Количество столбцов в выводе должно быть наибольшим, но общая ширина строки не должна превышать M (предполагается, что M
достаточно велико, чтобы вместить один столбец). Ширина колонок под сомножители и произведения должна соответствовать максимальной
ширине соответствующего значения (даже если в данной колонке данного столбца эта ширина не достигается, см. пример).
Таким образом все столбцы должны быть одинаковой ширины. Разделители вида "===…===" должны быть ширины M.
"""

import math

def print_multiplication_table(N, M):
    len_num = len(str(N))
    len2_num = len(str(N ** 2))
    max_len = len_num * 2 + len2_num + 3 + 3

    one_line_count = math.floor((M - max_len) / (max_len + 3)) + 1
    line_rows = math.ceil(N / one_line_count)

    form = "{:.>{}}.*.{:.<{}}.=.{:.<{}}"

    print("=" * M)

    for i in range(1, line_rows + 1):
        for second in range(1, N + 1):
            start = (i - 1) * one_line_count + 1
            end = i * one_line_count + 1 if i * one_line_count < N else N + 1

            for first in range(start, end):
                equation = form.format(first, len_num, second, len_num, first * second, len2_num)
                print(equation, end=(".|." if first != end - 1 else "\n"))

        print("=" * M)

N, M = map(int, input("").split(","))
print_multiplication_table(N, M)

