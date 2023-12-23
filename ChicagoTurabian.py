"""
Написать программу, которой на вход подаётся две строки — внутритекстовая ссылка N на некоторую книгу и библиографическая ссылка B на эту же книгу. программа должна проверить, что обе ссылки синтаксически верны и ссылаются на одну и ту же книгу. Формат ссылок — упрощённый стиль Турабьян. Вывод программы — True, если B соответствует N, и False — если не соответствует, или такое соответствие невозможно определить из-за синтаксической некорректности

Полное описание стиля для задачи с примерами

Обратите внимание на то, как в B слились точка после инициала автора и точка после списка авторов.

Будем считать, что страница может быть указана или одна, или диапазоном
Во всех примерах со страницами «–» — это не «—» и не «-». Серьёзно! А в интернете бывает все три.

Будем считать, что у первого автора всегда есть и имя, и фамилия
Никаких вложенных скобок!
Обратите внимание на т. н. «оксфордскую запятую» перед словом «and» в перечне авторов: она не соблюдается только для двух авторов в N, а в остальных случаях — для трёх и более авторов в N и для двух и более авторов в B — соблюдается)


42. Roger Frey, Utility and Rights (Minneapolis: University of Minnesota Press, 1984), 95.
Frey, Roger. Utility and Rights. Minneapolis: University of Minnesota Press, 1984.
Можно проверить с помощью примеров с оф. сайта (только раздел «BOOK») и вообще поиском «chicago turabian citation» (если в примере присутствует редактор, том, сайт и прочее, его придется сначала почистить)

Подсказка: Не пытайтесь всё запихнуть в РВ. не выйдет!

Я, например, с помощью РВ делаю проверку синтаксиса, выковыриваю поля из того варианта ссылки, где они однозначны, потом формирую возможные варианты представления N и сравниваю его с настоящим N

Особенно неприятно искать название книги. Потому что в нём могут быть и скобки, и точки, и имена. Единственное, что спасает: название — это то , что в N идёт между запятой и скобкой с местом печати, а в B — между точкой и точкой с местом печати (в примере — «,»…«(Minneapolis:» и «.»…«. Minneapolis:»)


True
"""



import re

def parse_N(reference):
    # Regex to capture various parts of the N reference
    authorN = r"(?P<authorN>[^.]+),\s"
    titleN = r"(?P<title>.+)\s\("
    cityN = r"(?P<city>.+):\s"
    publisherN = r"(?P<publisher>.+),\s"
    dateN = r"(?P<date>\d+)\)"
    Nt = authorN + titleN + cityN + publisherN + dateN

    match_N = re.search(Nt, reference)
    if match_N:
        return match_N.groupdict()
    return None

def parse_B(reference):
    # Regex to capture various parts of the B reference
    authorB = r"(?P<authorB>[^.]+)\.\s"
    titleB = r"(?P<title>.+)\.\s"
    cityB = r"(?P<city>.+):\s"
    publisherB = r"(?P<publisher>.+),\s"
    dateB = r"(?P<date>\d+)\."
    Bt = authorB + titleB + cityB + publisherB + dateB

    match_B = re.search(Bt, reference)
    if match_B:
        return match_B.groupdict()
    return None

def standardize_authors(authors):
    # Standardize author names to a common format for comparison
    authors = authors.replace(" and ", ", ").replace(" et al.", "")
    author_list = authors.split(", ")
    standardized = set()
    for author in author_list:
        parts = author.split(" ")
        if len(parts) > 1:
            standardized.add(parts[-1] + ", " + " ".join(parts[:-1]))
    return standardized

def compare_references(N, B):
    if N is not None and B is not None:
        authors_N = standardize_authors(N["authorN"])
        authors_B = standardize_authors(B["authorB"])
        return (authors_N == authors_B and
                N["title"] == B["title"] and
                N["city"] == B["city"] and
                N["publisher"] == B["publisher"] and
                N["date"] == B["date"])
    return False

N_reference = input("Enter N reference: ")
B_reference = input("Enter B reference: ")

N_parsed = parse_N(N_reference)
B_parsed = parse_B(B_reference)

if compare_references(N_parsed, B_parsed):
    print("True")
else:
    print("False")
