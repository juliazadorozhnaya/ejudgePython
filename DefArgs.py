from inspect import signature


def DefArgs(*constants):
    def decorator(func):
        argum = len(signature(func).parameters)
        if len(constants) < argum:
            raise TypeError()

        def wrapper(*args, **kwargs):
            if len(args) > func.__code__.co_argcount:
                raise TypeError("Too many arguments for the decorated function")

            for i, arg in enumerate(args):
                if not isinstance(arg, type(constants[i])):
                    raise TypeError(f"Argument {i + 1} must be of type {type(constants[i])}")

            kwargs.update(zip(func.__code__.co_varnames[len(args):], constants[len(args):]))

            return func(*args, **kwargs)

        return wrapper

    return decorator


@DefArgs(2, 3, 4)
def mult(a, b):
    return a * b


for args in (), (4,), (7, 8), (7, 8, 9), ("q", "w"):
    try:
        print(mult(*args))
    except TypeError:
        print("Nope")

try:
    @DefArgs(2)
    def mult(a, b):
        return a * b
except TypeError:
    print("Nope")
