"""
Ввести два натуральных числа через запятую: N и M. Вывести таблицу умножения от 1 до N включительно в формате,
представленном ниже, разделяя колонки, если они есть, тремя символами «.|.» («.*.» и «.=.» также занимают по три символа).
Количество столбцов в выводе должно быть наибольшим, но общая ширина строки не должна превышать M (предполагается, что M
достаточно велико, чтобы вместить один столбец). Ширина колонок под сомножители и произведения должна соответствовать максимальной
ширине соответствующего значения (даже если в данной колонке данного столбца эта ширина не достигается, см. пример).
Таким образом все столбцы должны быть одинаковой ширины. Разделители вида "===…===" должны быть ширины M.
"""

numbers = eval(input())
n = numbers[0]
m = numbers[1]

kn = n
slaglength = 0

while (kn >= 1):
    slaglength = slaglength + 1
    kn = kn / 10

kn = n * n
sumlength = 0

while (kn >= 1):
    sumlength = sumlength + 1
    kn = kn / 10

kn = 0
strl = slaglength + 3 + slaglength + 3 + sumlength

maxcolc = int(m / strl)
strl = strl + (maxcolc - 1) * 3 / maxcolc
maxcolc = int(m / strl)
currentMn = 1
check = 0

while (kn <= n):
    check = 0
    for i in range(0, m):
        print('=', end='')

    print()

    for j in range(1, n + 1):
        for i in range(currentMn, currentMn + maxcolc):
            if (i <= n):
                check = 1
                if ((i < currentMn + maxcolc - 1) and (i != n)):
                    print("{f:<{slagl}} * {s:<{slagl}} = {t:<{suml}} | ".format(f=i, s=j, t=i * j, slagl=slaglength,
                                                                                suml=sumlength), end='')
                else:
                    print("{f:<{slagl}} * {s:<{slagl}} = {t:<{suml}}".format(f=i, s=j, t=i * j, slagl=slaglength,
                                                                             suml=sumlength), end='')
        print()

    currentMn = currentMn + maxcolc
    kn = kn + maxcolc

if (check == 1):
    for i in range(0, m):
        print('=', end='')
