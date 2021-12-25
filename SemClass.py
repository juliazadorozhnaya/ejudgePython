_semaphores = {}


class Lock:
    def __init__(self, value):
        self._value = value
        self._semaphore = None

    @property
    def lock(self):
        if self._semaphore:
            if self._semaphore not in _semaphores:
                _semaphores[self._semaphore] = self._value
                return self._semaphore
            else:
                if _semaphores[self._semaphore] == self._value:
                    return self._semaphore
        return None

    @lock.setter
    def lock(self, semaphore):
        self._semaphore = semaphore
        if self._semaphore in _semaphores:
            if _semaphores[self._semaphore] == self._value:
                _semaphores.pop(self._semaphore)

    @lock.deleter
    def lock(self):
        _semaphores.pop(self._semaphore, None)

    def locked(cls):
        cls.__init__ = Lock.__init__
        cls.__del__ = Lock.__del__
        cls.lock = Lock.lock
        return cls

    def __del__(self):
        if self._semaphore in _semaphores:
            if _semaphores[self._semaphore] == self._value:
                _semaphores.pop(self._semaphore, None)


