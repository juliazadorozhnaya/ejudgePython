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
    prefix = r"\d+\.\s"
    authorN = r"(?:" + r"(?P<author41>.+)\s(?P<author42>[^\s,]+)\set\sal\." + r"|" + r"(?P<author211>[^,]+)\s(?P<author212>\S+)\sand\s(?P<author22>[^,]+)" + r"|" + r"(?P<author11>[^,]+)\s(?P<author12>[^\s,]+)" + r"(?:(?:(?:,\s(?P<author3>.+),)?\sand\s(?P<author2>[^,]+)))?" + r")" + r",\s"
    titleN = r"(?P<title>.+)\s\("
    cityN = r"(?P<city>.+):\s"
    publisherN = r"(?P<publisher>.+),\s"
    dateN = r"(?P<date>\d+)\),\s"
    pageN = r"(?:(?:\d+|\d+-\d+))\."
    Nt = prefix + authorN + titleN + cityN + publisherN + dateN + pageN

    match_N = re.search(Nt, reference)
    if match_N:
        return {k: v for k, v in match_N.groupdict().items() if v is not None}
    return None



def parse_B(reference):
    authorB = r"(?P<author12>\S+),\s(?P<author11>[^,]+)(?:,(?:\s(?P<author3>[^,]+),)?(?:\s(?P<author4>[^,]+),)*\sand\s(?P<author2>[^\d]+))?" + r"\.\s"
    titleB = r"(?P<title>.+)\.\s"
    cityB = r"(?P<city>.+):\s"
    publisherB = r"(?P<publisher>.+),\s"
    dateB = r"(?P<date>\d+)\."
    Bt = authorB + titleB + cityB + publisherB + dateB

    match_B = re.search(Bt, reference)
    if match_B:
        return {k: v for k, v in match_B.groupdict().items() if v is not None}
    return None

N_reference = input()
B_reference = input()

N_parsed = parse_N(N_reference)
print(N_parsed)
B_parsed = parse_B(B_reference)
print(B_parsed)

if N_parsed is not None and B_parsed is not None and all(N_parsed.get(key) == B_parsed.get(key) for key in N_parsed):
    print("True")
else:
    print("False")