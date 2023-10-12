"""
Ввести через запятую шесть чисел: x1, y1, x2, y2, x3, y3 и
вывести точное значение площади треугольника (x1, y1), (x2, y2), (x3, y3).
"""
from decimal import Decimal, getcontext

getcontext().prec = 200

x1, y1, x2, y2, x3, y3 = map(Decimal, input().split(','))
area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / Decimal('2'))

print(area)
