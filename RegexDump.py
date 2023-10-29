import re

# Ввод регулярного выражения
regex_pattern = input("Введите регулярное выражение: ")

# Компиляция регулярного выражения
regex = re.compile(regex_pattern)

# Ввод строк поиска
search_strings = []
while True:
    search_string = input("Введите строку поиска (пустая строка для завершения): ")
    if not search_string:
        break
    search_strings.append(search_string)

# Поиск и вывод результатов
for search_string in search_strings:
    match = regex.search(search_string)
    if match:
        start_position = match.start()
        matched_string = match.group(0)
        print(f"{start_position}: {matched_string}")

        # Вывод информации о группах
        for group_name, group_value in match.groupdict().items():
            if group_value is not None:
                print(f"{group_name}/{start_position}: {group_value}")
    else:
        print("<NONE>")
