class Shared:
    objects = 0
    total = 0

    def __init__(self):
        Shared.objects += 1
        self.local = 0
        self.id = Shared.objects

    def __str__(self):
        return f'|{Shared.objects}/{Shared.objects - self.local}/{Shared.total}/{self.local}|'

    def __invert__(self):
        Shared.total += 1
        self.local += 1
        return self.local

b, c = Shared(), Shared()
print(b, c, Shared())
print(~c, ~b, ~c)
print(b, c)

