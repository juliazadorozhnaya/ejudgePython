from fractions import Fraction
from math import floor, ceil


class Sausage:
    PART_LENGTH = 12

    def __init__(self, base="pork!", length=1):
        self.base = base
        self.length = Fraction(length)
        if self.length < 0:
            self.length = Fraction(0, 1)

    @property
    def full_parts(self):
        return floor(self.length)

    @property
    def last_part(self):
        d = self.length - floor(self.length)
        return d.numerator * floor(12 / d.denominator)
    
    @staticmethod
    def expand_string(s, n):
        return (s * (n // len(s) + 1))[:n]

    def __repr__(self):
        s = ""
        for _ in range(self.full_parts):
            s += "/" + "-" * Sausage.PART_LENGTH + "\\"
        if self.last_part or self.full_parts == 0:
            s += "/" + "-" * self.last_part + "|"
        s += "\n"

        for _ in range(3):
            for i in range(self.full_parts):
                s += "|" + Sausage.expand_string(self.base, Sausage.PART_LENGTH) + "|"
            if self.last_part or self.full_parts == 0:
                s += "|" + Sausage.expand_string(self.base, self.last_part) + "|"
            s += "\n"

        for _ in range(self.full_parts):
            s += "\\" + "-" * Sausage.PART_LENGTH + "/"
        if self.last_part or self.full_parts == 0:
            s += "\\" + "-" * self.last_part + "|"

        return s

    def __add__(self, other):
        return Sausage(self.base, self.length + other.length)

    def __sub__(self, other):
        return Sausage(self.base, self.length - other.length)

    def __mul__(self, other):
        return Sausage(self.base, self.length * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return Sausage(self.base, self.length / other)

    def __abs__(self):
        return self.length

    def __bool__(self):
        return self.length != 0



