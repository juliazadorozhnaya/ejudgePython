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

notletter = re.compile(r"([^a-zA-Z']+)")
soglglasn = re.compile(r"([^aouie]+)([aouie]+.*)")
glasnsogld = re.compile(r"([aouie]+[^aouie]+)([aouie].*)")

def analyze(a):
    ans = []
    for item in notletter.split(a):
        if item:
            if notletter.search(item):
                ans.append(item)
            else:
                if item[0].lower() in "aouie":  # If the word starts with a vowel
                    if item[0].isupper():
                        item = item.lower()
                        if glasnsogld.match(item):  # Multi-syllabic word
                            tmp = glasnsogld.sub(r"\2\1ay", item)
                            ans.append(tmp[0].upper() + tmp[1:])
                        else:  # Single-syllable word
                            ans.append(item.capitalize() + "yay")
                    else:
                        if glasnsogld.match(item):  # Multi-syllabic word
                            ans.append(glasnsogld.sub(r"\2\1ay", item))
                        else:  # Single-syllable word
                            ans.append(item + "yay")
                else:  # If the word starts with a consonant
                    if item[0].isupper():
                        tmp = soglglasn.sub(r"\2\1ay", item.lower())
                        ans.append(tmp[0].upper() + tmp[1:])
                    else:
                        ans.append(soglglasn.sub(r"\2\1ay", item))
    return "".join(ans)


a = input()
while a:
    print(analyze(a))
    a = input()
