"""
Ввести построчно две строки и проверить, есть ли такое число n, что вторая строка получается из первой,
если сначала взять каждый n-й символ, затем — каждый n-й, начиная с первого и т. д.
до каждого n-го, начиная с n-1-го. Вывести наименьшее возможное n, а если такого числа нет — No.
"""

first_string = input()
second_string = input()

for n in range(1, min(len(first_string), len(second_string)) + 1):
    reconstructed_string = ''

    for i in range(n):
        reconstructed_string += first_string[i::n]

    if reconstructed_string == second_string:
        print(n)
        break
else:
    print("No")