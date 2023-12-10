import sys

KEYWORD = "Левин"
CODINGS = ["KOI8-R", "CP1251", "CP866", "MACCYRILLIC", "ISO-8859-5", "CP855"]
ALPH = """!"'(),-.0123456789:;?ABCDEFHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя \t\n"""

def _input_example():
    s = """     - Она не то  что  скучает,  но  эта  неопределенность,  нерешительность
    положения, - слышал Левин  и  хотел  поспешно  отойти;  но  Степан  Аркадьич
    подозвал его.
        - Левин! - сказал Степан Аркадьич, и  Левин  заметил,  что  у  него  на"""

    bytes = s.encode("KOI8-R")
    bytes = bytes.decode("CP1251").encode("KOI8-R")
    bytes = bytes.decode("CP1251").encode("CP866")
    bytes = bytes.decode("CP855").encode("MACCYRILLIC")

    return bytes

def reverse_coding(word, i, j):
    try:
        return word.decode(CODINGS[i]).encode(CODINGS[j])
    except UnicodeDecodeError:
        return None

def generate_coding_indices():
    indices = range(len(CODINGS))
    for i in indices:
        for j in indices:
            if i != j:
                yield (i, j)

def restore_text(encoded_text):
    target_map = {ALPH.encode("KOI8-R"): KEYWORD.encode("KOI8-R")}
    codings_map = {ALPH.encode("KOI8-R"): ["KOI8-R"]}

    arr = [ALPH.encode("KOI8-R")]

    while arr:
        word = arr.pop()
        for i, j in generate_coding_indices():
            new_word = reverse_coding(word, i, j)
            if new_word is not None and new_word not in codings_map:
                codings_map[new_word] = codings_map[word] + [CODINGS[i], CODINGS[j]]
                target_map[new_word] = reverse_coding(target_map[word], i, j)
                arr.append(new_word)

    for key, value in target_map.items():
        if value in encoded_text:
            counter = 0
            for step in reversed(codings_map[key]):
                if counter % 2 == 0:
                    encoded_text = encoded_text.decode(step)
                else:
                    encoded_text = encoded_text.encode(step)
                counter += 1
            break

    print(encoded_text)

# Пример использования
# input_bytes = _input_example()
input_bytes = sys.stdin.buffer.read()
restore_text(input_bytes)
