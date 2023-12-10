#!/usr/bin/env python3

import sys
import re

alphabet = r'[\x00-\x7FА-Я]+'


def check_koi8_r(encoded_string):
    try:
        decoded_string = encoded_string.decode('koi8-r')
    except:
        return False
    try:
        if decoded_string.split()[0] == 'ПРОЦ':
            return True
        return False
    except:
        return False


def find_decoding(input_string, encodings, depth=0, path=[]):
    if depth == len(path):
        try:
            decoded_string = input_string
            for encoding in path:
                decoded_string = decoded_string.decode(encoding)
            if check_koi8_r(decoded_string):
                if re.fullmatch(alphabet, decoded_string):
                    print(decoded_string.strip('%'))
                    sys.exit(0)
        except:
            pass
    else:
        for encoding in encodings:
            find_decoding(input_string, encodings, depth + 1, path + [encoding])


if __name__ == "__main__":
    encodings = 'cp037 cp1006 cp1250 cp1251 cp1253 cp1254 cp1255 cp1256 cp1257 cp1258 cp437 cp720 cp737 cp775 cp850 cp852 cp855 cp864 cp866 cp869 cp874 cp875 hp_roman8 iso8859_10 iso8859_16 iso8859_4 iso8859_5 koi8_r latin_1 mac_croatian mac_greek mac_iceland mac_latin2'.split()

    inp = sys.stdin.read()
    small_check = inp.split('\n')[0]

    find_decoding(small_check.encode(), encodings)
