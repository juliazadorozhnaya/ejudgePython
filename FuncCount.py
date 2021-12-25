from functools import wraps


def counter(func):
    func.count = 0

    def method():
        return func.count

    func.counter = method

    @wraps(func)
    def wrapper(*args, **kwargs):
        func.count += 1
        return func(*args, **kwargs)

    return wrapper

