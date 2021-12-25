class DivStr(str):
    def __init__(self, line=''):
        self.__line = line

    def __str__(self):
        return self.__line

    def __len__(self):
        return len(self.__line)

    def __mul__(self, other):
        return DivStr(self.__line * other)

    def __rmul__(self, other):
        return DivStr(self.__line * other)

    def __add__(self, other):
        return DivStr(self.__line + other)

    def __radd__(self, other):
        return DivStr(other + self.__line)

    def __getitem__(self, other):
        return DivStr(self.__line.__getitem__(other))

    def capitalize(self, *args, **kwargs):
        return DivStr(self.__line.capitalize(*args, **kwargs))

    def casefold(self, *args, **kwargs):
        return DivStr(self.__line.casefold(*args, **kwargs))

    def center(self, *args, **kwargs):
        return DivStr(self.__line.center(*args, **kwargs))

    def ljust(self, *args, **kwargs):
        return DivStr(self.__line.ljust(*args, **kwargs))

    def rjust(self, *args, **kwargs):
        return DivStr(self.__line.rjust(*args, **kwargs))

    def lower(self, *args, **kwargs):
        return DivStr(self.__line.lower(*args, **kwargs))

    def replace(self, *args, **kwargs):
        return DivStr(self.__line.replace(*args, **kwargs))

    def lstrip(self, *args, **kwargs):
        return DivStr(self.__line.lstrip(*args, **kwargs))

    def rstrip(self, *args, **kwargs):
        return DivStr(self.__line.rstrip(*args, **kwargs))

    def strip(self, *args, **kwargs):
        return DivStr(self.__line.strip(*args, **kwargs))

    def title(self, *args, **kwargs):
        return DivStr(self.__line.title(*args, **kwargs))

    def swapcase(self, *args, **kwargs):
        return DivStr(self.__line.swapcase(*args, **kwargs))

    def upper(self, *args, **kwargs):
        return DivStr(self.__line.upper(*args, **kwargs))

    def zfill(self, *args, **kwargs):
        return DivStr(self.__line.zfill(*args, **kwargs))

    def translate(self, *args, **kwargs):
        return DivStr(self.__line.translate(*args, **kwargs))

    def removeprefix(self, *args, **kwargs):
        return DivStr(self.__line.removeprefix(*args, **kwargs))

    def removesuffix(self, *args, **kwargs):
        return DivStr(self.__line.removesuffix(*args, **kwargs))

    def join(self, *args, **kwargs):
        return DivStr(self.__line.join(*args, **kwargs))

    def __floordiv__(self, other):
        if other == 0:
            return []
        s = ''
        div_list = []
        block_size = len(self) // other
        if block_size == 0:
            return [''] * other
        for i, x in enumerate(self.__line):
            if i % block_size == 0 and i != 0:
                div_list.append(DivStr(s))
                s = ''
            s += x
        if len(s) == block_size:
            div_list.append(DivStr(s))
        return div_list

    def __mod__(self, other):
        if other == 0:
            return None
        last_part_size = len(self) % other
        return DivStr(self.__line[-last_part_size:]) if last_part_size != 0 else DivStr('')
