"""
Ввести натуральное число N и вывести, сколько ∃ различных пар натуральных чисел A и B: A³+B³=N
(с точностью до перестановки). Вещественные операции (например, кубический корень)
рекомендуется использовать как можно реже.
"""

import math

def CubeSum():
    N = int(input())
    count = 0
    limit = int(math.ceil(N ** (1/3)))

    for A in range(1, limit + 1):
        for B in range(A, limit + 1):
            if A**3 + B**3 == N:
                count += 1
    return count

print(CubeSum())