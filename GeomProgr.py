class Geom:
    def __init__(self, base, ratio):
        self.base = base
        self.ratio = ratio

    def __iter__(self):
        return self

    def __next__(self):
        result = self.base
        self.base *= self.ratio
        return result

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            if step < 0:
                return []
            result = []
            for i in range(start, stop, step):
                result.append(self.base * (self.ratio ** i))
            return result
        else:
            return self.base * (self.ratio ** key)

    def __repr__(self):
        return f"Geom({self.base}, {self.ratio})"


g = Geom(3, 2)
print(*zip("012345", g))
print(*g[:6])
print(*g[10::-2])
print(*zip(g[...], "0123"))
print(*g[3, ..., 11])
