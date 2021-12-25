import sys
import random


def create_words(txt, n):
    return [txt[i:i+n] for i in range(len(txt) - n + 1)]


def create_dict(list_words):
    result_dict = {}
    for words in list_words:
        result_dict.setdefault((words[0], words[1]), [])
        result_dict[(words[0], words[1])].append(words[2])
    return result_dict


def create_result(dict_words, L):
    result = []
    dict_keys = list(dict_words.keys())
    temp = random.choice(dict_keys[:len(dict_keys) // 2])
    result.extend(temp)
    for i in range(L - 2):
        temp = random.choice(dict_words[(result[i], result[i + 1])])
        result.append(temp)
    return ' '.join(word if '@' not in word else "\n    " for word in result)


L = int(input())
txt = sys.stdin.read().replace("\n    ", " @ ").split()
list_words = create_words(txt, 3)
dict_words = create_dict(list_words)
result = create_result(dict_words, L)
print(result)
