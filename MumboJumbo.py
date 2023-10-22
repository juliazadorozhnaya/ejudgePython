"""
Ввод представляет собой строки из букв латинского алфавита (последняя строка — пустая). Это письмена на языках двух племён:
Mumbo и Jumbo. Чётные строки — слова одного языка, нечётные — другого (какого — неизвестно). Языки Mumbo и Jumbo имеют
одинаковые гласные и разные согласные, причём согласных в языке Mumbo больше, чем в Jumbo. Все слова начинаются на гласную.
Определить и вывести, какому языку — Mumbo или Jumbo — принадлежит первое слово, если известно, что в данном корпусе текстов:
Использованы все начальные гласные (буква, на которую не начинается ни одно слово — согласная) Использованы все согласные
"""


def Mumbo_Jumbo():
    first_letters = set()
    second_letters = set()
    flag = True
    first_word = []

    while True:
        word = input()
        if not word:
            break

        if flag:
            first_letters |= set(word)
        else:
            second_letters |= set(word)

        if len(first_word) == 0:
            first_word.append(word)

        flag = not flag

    letter = {'a', 'e', 'i', 'o', 'u'}
    first_letters -= letter
    second_letters -= letter

    if len(first_letters) > len(second_letters):
        return "Mumbo"
    else:
        return "Jumbo"


print(Mumbo_Jumbo())
