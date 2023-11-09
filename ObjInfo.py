"""
Напишите класс Shared, экземпляры которого будут обладать следующими свойствами: При выводе с помощью print() должно выводиться
строка вида «|objects/live/total/local|, где objects — количество созданных за всё время экземпляров класса Shared (без учёта их удаления),
live — количество актуальных экземпляров класса Shared, total — сколько всего операций «~» применялось к объектам класса Shared, а local —
сколько операций «~» применялось к данному объекту Операция ~объект должна возвращать число local (уже увеличенное на 1 ☺)
"""

class Shared:
    objects = 0
    live = 0
    total = 0

    def __init__(self):
        Shared.objects += 1
        Shared.live += 1
        self.local = 0

    def __del__(self):
        Shared.live -= 1

    def __repr__(self):
        return f"|{Shared.objects}/{Shared.live}/{Shared.total}/{self.local}|"

    def __invert__(self):
        self.local += 1
        Shared.total += 1
        return self.local
