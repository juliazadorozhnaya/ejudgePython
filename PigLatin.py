import re

def hog_latin_word(match):
    word = match.group()
    if word.isalpha():
        if word[0].isupper():
            return re.sub(r'^([^aeiouAEIOU]+)(.*)', r'\2\1ay', word).capitalize()
        elif word[0].islower():
            return re.sub(r'^([^aeiouAEIOU]+)(.*)', r'\2\1ay', word)

        else:
            return word + 'yay'
    else:
        return word

def hog_latin_text(text):
    pattern = r'\b[a-zA-Z]*[a-zA-Z]\b'
    translated_text = re.sub(pattern, hog_latin_word, text)
    return translated_text

# Ввод текста и вывод поросячей латыни
input_text = ""
line = input()
while line:
    input_text += line + "\n"
    line = input()

translated_text = hog_latin_text(input_text)
print(translated_text, end='')

#Isthay isyay anyay ampleexay ofyay Oghay Atinlay. Asyay ouyay ancay eesay, it'syay illysay,
#utbay otslay ofyay unfay orfay ildrenchay.

