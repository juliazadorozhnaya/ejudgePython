"""
Ввести натуральное число N и вывести, сколько ∃ различных пар натуральных чисел A и B: A³+B³=N
(с точностью до перестановки). Вещественные операции (например, кубический корень)
рекомендуется использовать как можно реже.
"""

def CubeSum(N):
    A = 1
    B = int(N ** (1 / 3))

    count = 0

    while A <= B:
        cubic_sum = A ** 3 + B ** 3
        if cubic_sum == N:
            count += 1

        if cubic_sum > N:
            B -= 1
        else:
            A += 1

    return count

N = int(input())
result = CubeSum(N)
print(result)
