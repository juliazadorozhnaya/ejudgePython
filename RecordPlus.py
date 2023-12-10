def Record(slots_str, **fields):
    def decorator(cls):
        class Wrapped(cls):
            __slots__ = sorted(slots_str.split())

            def __iter__(self):
                return iter(sorted(self.__slots__ + [field for field in fields if not field.startswith("_")]))

            def __str__(self):
                return "|".join(f"{attr}={getattr(self, attr)}" if hasattr(self, attr) else attr for attr in self)

        for field, value in fields.items():
            if not field.startswith("_"):
                setattr(Wrapped, field, property(lambda self, value=value: value))

        return Wrapped

    return decorator
