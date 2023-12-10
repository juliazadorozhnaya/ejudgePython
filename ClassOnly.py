
class Struct:
    def __getattribute__(self, item):
        if item.startswith('_') or (len(item) == 4 and all(char in 'abcd' for char in item)):
            return item
        else:
            raise AttributeError

from itertools import product
from collections import Counter

lst = [Struct() for i in range(1000000)]
FIELDS = ["".join(q) for q in product(*(["abcd"] * 4))]
res = Counter(getattr(l, FIELDS[i % len(FIELDS)]) for i, l in enumerate(lst))
print(sorted(set(res.values())))