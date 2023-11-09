"""
Согласно правилам «поросячьей латыни» английские слова при разговоре преобразуются так:

Если слово начинается на согласную — эта согласная переносится в конец слова, после чего добавляется «ay»: "latin" ⇒ "atinlay"

Если слово начинается на несколько согласных, они все переносятся в конец слова, после чего добавляется «ay»: "stupid" ⇒ "upidstay"

Если слово начинается на гласную, "aouie" (не "y"!) и имеет более одного слога, лидирующие гласные и все согласные за ними переносятся в конец с добавлением «ay»: "under" ⇒ "erunday" (в Википедии это второй вариант)

для нашего удобства непроизносимые гласные тоже считаются слогом, например "are" ⇒ "earay"; (так исторически не было: язык всё-таки разговорный)

Односложные слова, начинающиеся на гласную, просто дополняются «yay»: "egg" ⇒ "eggyay"

Последовательности, состоящие только из согласных, не изменяются (например, такой последовательностью является «my»)

Апостроф считается согласной буквой (маленькой), а дефис — разделителем (опять-таки для простоты)

Написать программу, которая построчно вводит «английский» текст (текст, содержащий последовательности латинских букв и другие символы; последняя строка пустая) и выводит перевод на поросячью латынь (для простоты любая последовательность английских букв с гласными считается словом). Обратите внимание на то, что слово, написанное со заглавной буквы, в поросячьей латыни также пишется со заглавной буквы. Более одной заглавной буквы в слове не встречается.


This is an example of Hog Latin. As you can see, it's silly,
but lots of fun for children.

Isthay isyay anyay ampleexay ofyay Oghay Atinlay. Asyay ouyay ancay eesay, it'syay illysay,
utbay otslay ofyay unfay orfay ildrenchay.
"""

import re

word = re.compile(r"([a-z']+)|([A-Z'][a-z']*)")
vowels = r"[eaoui]"
firstvow = r"([eaoui])([a-z']*)"
firstvowcons = r"([aouie])([^aouie]*)([aouie])([a-z']*)"
firstcons = r"([^aouie]+)([aouie])([a-z']*)"

def translateword(s):
    flag = False
    if s[0].isupper():
        flag = not flag
    s = s.lower()

    if re.fullmatch(firstvow, s) is not None:
        if len(re.findall(vowels, s)) == 1:
            res = re.sub(firstvow, r"\1\2yay", s)
        else:
            res = re.sub(firstvowcons, r"\3\4\1\2ay", s)

    elif re.fullmatch(firstcons, s) is not None:
        res = re.sub(firstcons, r"\2\3\1ay", s)

    else:
        return s[0].upper() + s[1::] if flag else s
    if flag:
        return res[0].upper() + res[1::]
    else:
        return res

string = input()
while bool(string):
    res = word.sub(lambda x: translateword(x.group()), string)
    print(res)
    string = input()