from functools import wraps


def cast(type):
    def functional(func):
        @wraps(func)
        def argument(*args):
            return type(func(*args))

        return argument

    return functional

