import re

def parse_reference(reference):
    # Регулярное выражение для разбора библиографической ссылки
    pattern = r'^(\d+)\. ([\w\s]+)(?:, and)? ([\w\s]+)\. ([\w\s]+): ([\w\s]+), (\d+), (\d+)\.$'
    match = re.match(pattern, reference)
    if match:
        return match.group(2), match.group(3), match.group(4), match.group(5), match.group(6)
    return None

def compare_references(ref1, ref2):
    # Разбор обеих ссылок
    parsed_ref1 = parse_reference(ref1)
    parsed_ref2 = parse_reference(ref2)

    if parsed_ref1 is None or parsed_ref2 is None:
        return False

    # Сравнение данных из ссылок
    author1, title1, publisher1, year1, page1 = parsed_ref1
    author2, title2, publisher2, year2, page2 = parsed_ref2

    return author1 == author2 and title1 == title2 and publisher1 == publisher2 and year1 == year2

# Ввод ссылок
reference1 = "42. Roger Frey, Utility and Rights (Minneapolis: University of Minnesota Press, 1984), 95."
reference2 = "Frey, Roger. Utility and Rights. Minneapolis: University of Minnesota Press, 1984."

# Проверка и сравнение ссылок
result = compare_references(reference1, reference2)
print(result)

