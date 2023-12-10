"""
Напишите класс FilterQueue со следующими свойствами:

Это потомок asyncio.Queue

В экземпляре класса атрибут очередь.window содержит первый элемент очереди, или None, если очередь пуста (просмотр очередь.window не влияет на состояние очереди)

С помощью операции фильтр in очередь можно определить, присутствуют ли в очереди такие элементы, что выражение фильтр(элемент) истинно

Метод .later() синхронно переставляет первый элемент очереди в её конец, или вызывает исключение asyncio.QueueEmpty, если очередь пуста

Метод .get() содержит необязательный параметр фильтр. Вызов очередь.get(фильтр) работает так:

Если в очереди нет элементов, на которых фильтр(элемент) истинно, работает как обычный .get().

Если в очереди есть элементы, на которых фильтр(элемент) истинно, переставляет первый элемент очереди в её конец до тех пор, пока фильтр(элемент) не истинно, а затем выполняет обычный .get().

Разрешается воспользоваться внутренним представлением Queue; код Queue можно посмотреть тут
"""

import asyncio

class FilterQueue(asyncio.Queue):
    @property
    def window(self):
        if self.empty():
            return None
        return self._queue[0]

    def __contains__(self, _filter):
        if _filter is None:
            return False
        else:
            for elem in self._queue:
                if _filter(elem):
                    return True
            return False

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        item = self.get_nowait()
        self.put_nowait(item)

    async def get(self, _filter=lambda x: None):
        if _filter not in self:
            return await super().get()

        while not _filter(self.window):
            self.later()

        return await super().get()
