"""
Ввести строку, содержащую произвольные символы (кроме символа «@»). Затем ввести строку-шаблон, которая может содержать
символы '@'. Проверить, содержится ли в исходной строке подстрока, совпадающая со строкой-шаблоном везде,
кроме символов '@'; на месте '@' в исходной строке должен стоять ровно один произвольный символ. Вывести наименьшую позицию в строке,
с которой начинается эта подстрока, или '-1', если её там нет. Использовать регулярные выражения нельзя! ☺
"""

def check(s, p):
    counter = 0
    start = 0
    good_index = -1
    while start < len(s):
        if s[start] == p[counter] or p[counter] == '@':
            if counter == 0:
                good_index = start
            counter += 1
        else:
            if counter != 0:
                if good_index != -1:
                    start = good_index
                else:
                    start -= 1
            counter = 0
        start += 1
        if counter == len(p):
            return good_index
    return good_index if counter == len(p) else -1


s = input()
p = input()

result = check(s, p)
print(result)