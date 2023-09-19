"""
Ввести в столбик последовательность целых (положительных и отрицательных) чисел, не равных нулю; в конце этой
последовательности стоит 0. Вывести наибольшую сумму последовательно идущих элементов
этой последовательности (не менее одного).
"""

def MaxSumsum():
    max_sum, current_sum = 0,0
    negative_max = float('-inf')

    while True:
        num = int(input())

        if num == 0:
            break

        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        elif current_sum < 0:
            current_sum = 0

        if num < 0 and num > negative_max:
            negative_max = num

    if max_sum != 0:
        return max_sum
    else:
        return negative_max

print(MaxSumsum())
