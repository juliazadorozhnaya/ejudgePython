"""
Написать класс Tester, при создании экземпляра которого ему передаётся единственный параметр — некоторая функция fun.
Сам экземпляр должен быть callable, и принимать два параметра — последовательность кортежей suite и необязательная (возможно, пустая)
последовательность исключений allowed. При вызове должна осуществляться проверка, можно ли функции fun() передавать каждый
элемент suite в качестве позиционных параметров. Если исключений не возникло, результат работы — 0, если исключения попадали под
классификацию одного из allowed, результат — -1, если же были исключения не из allowed — 1.

К. О. советует определить метод .__call__()
Спойлер: В клаузе except можно написать кротеж из исключений!
"""


class Tester:
    def __init__(self, func):
        self.func = func

    def __call__(self, suites, allowed=None, **kwargs):
        allowed = allowed or []
        errors = []
        for suite in suites:
            try:
                self.func(*suite)
            except Exception as e:
                errors.append(e)

        if not errors:
            return 0
        return -1 if all(isinstance(error, tuple(allowed)) or isinstance(error, Exception) for error in errors) else 1


def req(x):
    if x <= 0:
        return x + 1
    else:
        return 2 * x + req(x - 1)


T = Tester(req)
print(T((el,) for el in range(0, 100)))
print(T((el,) for el in range(200, 1500)))
