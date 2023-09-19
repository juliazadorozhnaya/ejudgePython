"""
Имеется большая последовательность объектов (неважно каких), допускающих операцию сравнения. Известно, что некоторых одинаковых
объектов в последовательности больше половины. Требуется, не храня последовательности, выяснить, чему они равны
(т. е. вывести пример такого объекта). Ввод построчный, последняя строка — пустая.
"""

def HalfMore():
    types_count = {}
    total_count = 0

    while True:
        line = input()
        if line == "":
            break
        total_count += 1
        if line in types_count:
            types_count[line] += 1
        else:
            types_count[line] = 1

    majority_type = max(types_count, key=types_count.get)
    return eval(majority_type)

print(HalfMore())

