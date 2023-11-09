"""
Написать класс Triangle, моделирующий треугольник: объект tri типа Triangle создаётся из трёх вещественных чисел — сторон треугольника
tri пуст, если не выполняется строгое неравенство треугольника или хотя бы одна из сторон не положительна abs(tri) — площадь треугольника
(0, если tri пуст) два объекта tri1 и tri2 типа Triangle равны, только если попарно равны их стороны (в некотором порядке) равенство
необходимо определять с помощью isclose() сравнение на неравенство двух объектов типа Triangle есть результат сравнения их площадей (независимо от того,
равны ли треугольники в указанном выше смысле) (на всякий случай) площадь вычисляется по формуле Герона строковое
представление: a:b:c, где a, b и c — это стороны треугольника в порядке их задания
"""

import math

class Triangle:
    sides = []

    a = 0
    b = 0
    c = 0
    emp = 0

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.sides = [float(a), float(b), float(c)]

        if (self.a <= 0) or (self.b <= 0) or (self.c <= 0) or (self.a + self.b < self.c) or (self.a + self.c < self.b) or (self.c + self.b < self.a):
            self.emp = 1

    def __bool__(self):
        if self.emp == 0:
            return True
        return False

    def __abs__(self):
        if self.sides[0] + self.sides[1] <= self.sides[2] or self.sides[1] + self.sides[2] <= self.sides[0] or self.sides[0] + self.sides[2] <= self.sides[1]:
            return 0
        p = sum(self.sides) / 2
        return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))

    def __str__(self):
        s = ""
        sides = [self.sides[0], self.sides[1], self.sides[2]]
        s += "{:.1f}".format(sides[0])
        s += ":{:.1f}".format(sides[1])
        s += ":{:.1f}".format(sides[2])
        return s

    def __eq__(self, other):
        return all(i == j for i, j in zip(sorted(self.sides), sorted(other.sides)))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)
