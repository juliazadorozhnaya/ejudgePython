"""
Ввести по одному в строке целые числа, не равные нулю (не менее одного, конец ввода — 0), вывести второй максимум
последовательности (число, строго меньшее максимума последовательности, и не меньшее остальных чисел в ней), и NO,
если такового нет.
"""
def SecondMax():
    numbers = set()
    while True:
        num = int(input())
        if num == 0:
            break
        numbers.add(num)


    if len(numbers) < 2:
        return "NO"
    else:
        max1 = max(numbers)
        numbers.remove(max1)
        max2 = max(numbers)
        print

    return max2

print(SecondMax())
