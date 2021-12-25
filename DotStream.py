class Dots:
    def __init__(self, left, right):
        self.left, self.right = left, right

    def __getitem__(self, val):
        if isinstance(val, int):
            return self._all_(val)
        else:
            start, step, stop = val.start, val.step, val.stop
            if (not step) and (start is not None) and (stop is not None):
                return self._get_point_(start, stop)
            else:
                return self._get_slice_(start, stop, step)

    def _all_(self, size):
        return self._get_slice_(0, size, size)

    def _length_(self, size):
        return (self.right - self.left) / (size - 1)

    def _get_point_(self, ind, size):
        return ind * self._length_(size) + self.left

    def _get_slice_(self, frm, to, size):
        if frm is None:
            frm = 0
        if to is None:
            to = size
        for num in range(frm, to):
            yield self._get_point_(num, size)