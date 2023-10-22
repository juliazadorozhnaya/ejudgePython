"""
Ввести построчно текст, состоящий из пробелов, переводов строки и латинских букв, и заканчивающийся пустой строкой.
Вывести слово, которое чаще других встречается в тексте, если оно такое одно, и ---, если таких слов несколько.
"""


from collections import Counter


def find_most_common_word():
    word_counter = Counter()
    while True:
        line = input()
        if not line:
            break
        words = line.split()
        word_counter.update(words)

    most_common_words = word_counter.most_common()

    if len(most_common_words) > 1 and most_common_words[0][1] == most_common_words[1][1]:
        return '---'
    else:
        return most_common_words[0][0]


result = find_most_common_word()
print(result)
