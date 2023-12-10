class positioned(type):
    def __new__(cls, name, bases, namespace):
        annotations = namespace.get("__annotations__", {})
        fields = list(annotations.keys())

        def __init__(self, *args):
            for attr, value in zip(fields, args):
                setattr(self, attr, value)

        def __str__(self):
            return ' '.join(f"{attr}={getattr(self, attr)}" for attr in fields)

        def __match_args__(self):
            return tuple(getattr(self, attr) for attr in fields)

        namespace["__init__"] = __init__
        namespace["__str__"] = __str__
        namespace["__match_args__"] = __match_args__

        return super().__new__(cls, name, bases, namespace)



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