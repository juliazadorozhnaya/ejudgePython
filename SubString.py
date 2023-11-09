"""
Реализовать класс SubString, который бы полностью воспроизводил поведение str, но вдобавок бы поддерживал операцию вычитания строк.
Вычитание устроено так: «уменьшаемое» просматривается посимвольно, и если соответствующий символ присутствует в «вычитаемом»,
то он однократно удаляется из обеих строк. Исходные объекты не меняются; то, что осталось от уменьшаемого, объявляется
результатом вычитания. К моменту прохождения теста ничего нового, кроме класса SubString в глобальном пространстве имён быть не должно
"""
from collections import UserString

class SubString(UserString):
    def __sub__(self, other):
        other_data = other.data if isinstance(other, SubString) else other

        from collections import Counter
        other_counter = Counter(other_data)
        result_chars = []

        for char in self.data:
            if char in other_counter and other_counter[char] > 0:
                other_counter[char] -= 1
            else:
                result_chars.append(char)

        return self.__class__("".join(result_chars))

del UserString
