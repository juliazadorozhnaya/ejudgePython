from inspect import getmembers, ismethod, signature
from numbers import Number

def dumper(cls):
    class DumperWrapper(cls):
        def __str__(self):
            attributes = []
            for name, value in getmembers(self):
                if not name.startswith("_"):
                    if isinstance(value, (Number, str)):
                        attributes.append(f"{name}={value}")
                    elif ismethod(value):
                        parameters = ', '.join(list(signature(value).parameters.keys()))
                        attributes.append(f"{name}({parameters})")
                    else:
                        attributes.append(f"{name}: {type(value).__name__}")
            return '; '.join(attributes)
    return DumperWrapper

