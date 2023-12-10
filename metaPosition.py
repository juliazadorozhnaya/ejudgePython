class positioned(type):
    def __new__(cls, name, bases, dct):
        annotations = dct.get("__annotations__", {})
        field_names = list(annotations.keys())

        def __init__(self, *args):
            for i, arg in enumerate(args):
                setattr(self, field_names[i], arg)

        def __str__(self):
            return ' '.join(f'{field}={getattr(self, field)}' for field in field_names)

        dct["__init__"] = __init__
        dct["__str__"] = __str__

        return super().__new__(cls, name, bases, dct)

# Пример использования
class C(metaclass=positioned):
    a: int = 1
    b: float = 42.0

for c in C(), C(4), C(100.0, 500), C(7, 2):
    print(c)
    match c:
        case C(1):
            print("C1", c.b)
        case C(b=42):
            print("C42", c.a)
        case C(100, 500):
            print("C100500")
        case C():
            print("C", c)
