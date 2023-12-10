"""
Написать параметрический декоратор (функцию или класс) DefArgs(*константы), которым можно декорировать функции
с фиксированным числом позиционных параметров. Возвращаемая им функция должна принимать произвольное количество позиционных
параметров, не большее чем у исходной функции. Все опущенные параметры должны получать соответствующие их позиции значения
из кортежа константы. Если констант меньше, чем параметров декорируемой функции, декоратор инициирует исключение TypeError.
Это же исключение инициируется при вызове функции со слишком большим количеством параметров. Дополнительно декоратор должен
проверять, что тип параметров при вызове соответствует типу констант, в противном случае также инициировать исключение TypeError.
"""

def DefArgs(*constants):
    def decorator(func):

        funcArg = func.__code__.co_argcount
        if len(constants) < funcArg:
            raise TypeError()

        def wrapper(*args):
            if len(args) > funcArg:
                raise TypeError()

            for i, arg in enumerate(args):
                if not isinstance(arg, type(constants[i])):
                    raise TypeError()

            far = args + constants[len(args):funcArg]

            return func(*far)

        return wrapper

    return decorator
