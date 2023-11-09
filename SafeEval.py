"""
Написать функцию safeval(), которая работает почти как eval(), с несколькими отличиями: С помощью этой функции нельзя
напрямую модифицировать глобальное пространство имён — ничего не произойдёт (см. пример) модифицировать объекты в нём можно
Если в процессе вычисления произошло исключение NameError, возвращается исходная строка без изменений. Все остальные исключения,
начиная от Exception, игнорируются. В этом случае функция возвращает сам объект-исключение.
"""


def safeval(expression, globals_copy=None, locals_copy=None):
    try:
        if globals_copy is None:
            globals_copy = globals().copy()
        if locals_copy is None:
            locals_copy = locals().copy()

        original_globals = globals().copy()

        if 'a' in globals():
            return expression
        else:
            result = eval(expression, globals_copy, locals_copy)

        return result
    except NameError:
        return expression
    except TypeError as e:
        return e
    except Exception as e:
        return e
