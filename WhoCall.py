"""
Написать функцию whocall(depth=1), которая возвращает имя и названия параметров (строкой через пробел) одной из функций,
вызов которой привёл к вызову whocall(). При depth=1 это функция, непосредственно вызвавшая whocall(), при depth=2 — функция,
которая вызвала эту функцию и т. д. При depth=0 это сама whocall(). Если вызывающий объект не является функцией (например, это модуль)
или depth превышает глубину стека вызовов, названия параметров — пустая строка;
в последнем случае в качестве имени возвращается <UNIVERSE>.
"""

import types
import inspect


def whocall(depth=1):
    stack = inspect.stack()

    try:
        # Получаем кадр стека для заданной глубины
        frame = stack[depth][0]

        # Получаем объект-функцию из кода кадра
        code = frame.f_code
        function = types.FunctionType(code, frame.f_globals, name=code.co_name)

        # Получаем сигнатуру функции
        signature = inspect.signature(function)

        # Убираем звездочки для *args, kw и **kwargs, а также для параметров, начинающихся с ** или *
        parameters = ' '.join(
            str(param)[2:] if str(param).startswith('**') else str(param)[1:] if str(param).startswith('*') else str(
                param) for param in signature.parameters.values())

        return code.co_name, parameters

    except IndexError:
        return '<UNIVERSE>', ''

