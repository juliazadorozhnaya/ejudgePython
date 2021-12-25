import sys


def create_encodes(goods, pattern):
    encoding = "cp1026 cp1140 cp1256 cp273 cp437 cp500 cp775 cp850 cp852 cp855 cp857 cp860 cp861 cp862 cp863 cp865 cp866 gb18030 hp_roman8 iso8859_10 iso8859_11 iso8859_13 iso8859_14 iso8859_15 iso8859_16 iso8859_2 iso8859_4 iso8859_5 iso8859_9 koi8_r mac_cyrillic mac_greek mac_latin2 mac_roman utf_8".split()
    pattern_compile = pattern.encode('utf-8')

    for i in encoding:
        for j in encoding:
            if i != j:
                try:
                    check = pattern_compile.decode(i).encode(j)
                    if pattern_compile == check.decode(j).encode(i):
                        goods.append((i, j))
                except Exception as e:
                    pass


def decode(data, goods, pattern, counter):
    if counter > 3:
        return
    if goods:
        for enc_1, enc_2 in goods:
            try:
                pattern_dec = pattern.decode(enc_1).encode(enc_2)
                if pattern == pattern_dec.decode(enc_2).encode(enc_1):
                    if data.find(pattern_dec) != -1:
                        result = data.decode(enc_2).encode(enc_1)
                    else:
                        result = decode(
                            data, goods, pattern_dec, counter + 1
                        ).decode(enc_2).encode(enc_1)
                    if counter == 1:
                        return result.decode('utf-8')
                    return result
            except Exception as e:
                pass


pattern = ", что"
data = sys.stdin.buffer.read()
goods = []
create_encodes(goods, pattern)
result = decode(data, goods, pattern.encode('utf-8'), 1)
print(result.split('\n')[0])