"""
Написать программу, которой на вход подаётся синтаксически верное регулярное выражение, а затем — строки поиска (последняя строка пустая). Программа должна выводить информацию о первой найденной в строке поиска подстроке, соответствующей регулярному выражению, в таком формате:

Если подстрока не найдена, выводится «<NONE>»
Если подстрока найдена, выводится позиция: подстрока, где «позиция» — это номер символа в строке, начиная с которого была найдена подстрока
Если в регулярном выражении присутствовала группировка с сохранением (попросту скобочки), выводится номер группы/позиция: подстрока для каждой группы
Если в регулярном выражении присутствовали именованные группы, выводится имя группы/позиция: подстрока для каждой группы (в порядке их появления в re.Match.groupdict())
Если какая-то группа присутствует в исходном выражении, но не нашла сопоставления (например, была помечена повторителем * и пропущена), она не выводится
"""

from re import *


def analyze(pattern, input_str):
    match = pattern.search(input_str)
    if match:
        print(match.start(), ": ", match.group(), sep="")

        for group_number, group_value in enumerate(match.groups()):
            if group_value:
                print(group_number + 1, "/", match.start(group_number + 1), ": ", group_value, sep="")

        for group_name, group_value in match.groupdict().items():
            if group_value:
                print(group_name, "/", match.start(group_name), ": ", group_value, sep="")
    else:
        print("<NONE>")


regex_pattern = input()
compiled_pattern = compile(regex_pattern)

search_strings = []

while True:
    search_string = input()

    if not search_string:
        break

    search_strings.append(search_string)

for search_string in search_strings:
    analyze(compiled_pattern, search_string)
