'''
Напишите класс Geom(база, знаменатель), задающий геометрическую прогрессию, нумерация членов которой идёт с нуля.
Сконструированный объект — бесконечная вычислимая последовательность, поддерживающая итерацию, индексирование и секционирование
(в том числе конструкции с умолчаниями). Дополнительно должно поддерживаться секционирование вида прогрессия[начало, ..., конец],
что соответствует конструкции прогрессия[начало:конец], причём параметр «начало ,» и/или «, конец» можно опускать.
Индексирование должно возвращать соответствующий член прогрессии, а секционирование — последовательность членов
(возможно, бесконечную). Конструкция прогрессия[::отрицательный шаг] возвращает пустую последовательность.
Известно, что база и знаменатель однотипны (проверять не надо), того же типа должны быть и члены последовательности.
'''


class Geom:
    def __init__(self, base, ratio):
        self.base = base
        self.ratio = ratio

    def __iter__(self):
        current = self.base
        while True:
            yield current
            current *= self.ratio

    def __getitem__(self, key):
        if isinstance(key, int):  # Single index
            if key < 0:
                raise IndexError()
            return self.base * (self.ratio ** key)

        if isinstance(key, tuple):  # Custom tuple slicing
            if len(key) == 2:  # Handling two elements
                start, end = key
                if start is Ellipsis:
                    start = 0
                if end is Ellipsis:
                    return self._infinite_slice(start)
                return [self[i] for i in range(start, end)]

            if len(key) == 3 and key[1] is Ellipsis:  # Handling three elements with Ellipsis
                start, _, end = key
                if start is None:
                    start = 0
                if end is None:
                    return self._infinite_slice(start)
                return [self[i] for i in range(start, end)]

        if isinstance(key, slice) or key is Ellipsis:  # Standard slicing or Ellipsis
            start, stop, step = (key.start, key.stop, key.step) if isinstance(key, slice) else (0, None, 1)
            start = start or 0  # Default start to 0

            # Handling negative steps
            if step is not None and step < 0:
                if stop is None:
                    stop = -1  # Default stop for negative step
                return [self[i] for i in range(start, stop, step)]

            # Handling positive steps
            if stop is None:
                return self._infinite_slice(start, step)
            else:
                return [self[i] for i in range(start, stop, step or 1)]

    def _infinite_slice(self, start, step=None):
        current = self.base * (self.ratio ** start)
        while True:
            yield current
            current *= self.ratio if step is None else self.ratio ** step
