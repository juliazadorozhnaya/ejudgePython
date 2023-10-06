"""
Ввести произвольное натуральное число, и вывести (через «*») все его разложения на натуральные сомножители,
превосходящие 1, без учёта перестановок. Сомножители в каждом разложении и сами разложения (как последовательности)
при выводе должны быть упорядочены по возрастанию. Само число также считается разложением.
Можно использовать рекурсию.
"""


def factorization(n, min_factor=2, curr_factor=[]):
    if n == 1:
        return [curr_factor]

    factorizations = []
    for f in range(min_factor, int(n ** 0.5) + 1):
        if n % f == 0:
            new_factor = curr_factor + [f]
            factorizations.extend(factorization(n // f, f, new_factor))

    if n >= min_factor:
        factorizations.append(curr_factor + [n])

    return factorizations


def print_factorization(factorizations):
    for f in factorizations:
        print("*".join(map(str, f)))


number = int(input())
factorizations = factorization(number)
print_factorization(factorizations)