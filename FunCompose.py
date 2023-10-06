"""
Написать функцию (точнее, функционал) compose(f, g), которому на вход подаётся два объекта-функции: f(x, y) от двух
параметров, и g(x₁, …, xₙ) от произвольного количества параметров. compose(f, g) должна возвращать функцию h()
от n параметров, являющуюся результатом применения f() к g(x₁, …, xₙ) (в прямом порядке) и g(xₙ, …, x₁) (в обратном порядке)
"""


def compose(f, g):
    def h(*args):
        result_forward = g(*args)
        result_backward = g(*reversed(args))
        return f(result_forward, result_backward)

    return h
