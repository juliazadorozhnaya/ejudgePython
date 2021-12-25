from types import FunctionType
from functools import wraps
import inspect
import re


pref = re.compile(r"__")


def checker(fun, name):
    @wraps(fun)
    def newf(self, *args, **kwargs):
        sig_obj = inspect.signature(fun)
        bind_obj = sig_obj.bind(self, *args, **kwargs)
        #print(sig_obj)
        #print(bind_obj)

        d = {}

        dhelp = sig_obj.parameters
        #for i in dhelp.items():
        #    print(i)

        for key, value in bind_obj.arguments.items():
            #print(key, value, sig_obj.parameters[key])
            #print(sig_obj.parameters[key].annotation)
            if sig_obj.parameters[key].annotation is not sig_obj.empty:
                d[key] = [value, sig_obj.parameters[key]]

        #print(d)
        infa = inspect.getfullargspec(fun)
        #print(infa)


        position_or_keyword = infa.args[1:]
        keyword = infa.kwonlyargs
        pos = infa.varargs
        named = infa.varkw
        #print(position_or_keyword, keyword, pos, named)
        #print(kwargs)

        #keyword += [pos, named] #################


        index = 0
        flag = 0
        for i in position_or_keyword:
            if i in d:
                #print("index", index, args[index])
                if not isinstance(args[index], d[i][1].annotation):
                    raise TypeError(f"Type mismatch: {i}")
            if len(args) > index + 1:
                index += 1
                #print(args, index)
            else:
                flag = 1
                break


        ostalos = len(position_or_keyword[index + 1:]) + len(keyword)
        #print(ostalos)

        if flag:
            for number, i in enumerate(kwargs):
                if i in d:
                    if not isinstance(kwargs[i], d[i][1].annotation):
                        raise TypeError(f"Type mismatch: {i}")


                elif i == pos:
                    if not isinstance(kwargs[i], dhelp[pos].annotation):
                        raise TypeError(f"Type mismatch: {pos}")


                if number == ostalos - 1:
                    break




            for i in kwargs:    #hz
                if not isinstance(kwargs[i], d[named][1].annotation):
                    raise TypeError(f"Type mismatch: {named}")

        else: #hz
            for i in keyword:
                if i in d:
                    if not isinstance(kwargs[i], d[i][1].annotation):
                        raise TypeError(f"Type mismatch: {i}")

            #print(args[index:], pos in d)
            if pos in d:
                for i in args[index:]:
                    if not isinstance(i, d[pos][1].annotation):
                        raise TypeError(f"Type mismatch: {pos}")


            if named in d:  #hz
                for i in kwargs:
                    if not isinstance(kwargs[i], d[named][1].annotation):
                        raise TypeError(f"Type mismatch: {named}")




        if sig_obj.return_annotation != sig_obj.empty:
            if not isinstance(fun(self, *args, **kwargs), sig_obj.return_annotation):
                raise TypeError(f"Type mismatch: return")

        return fun(self, *args, **kwargs)
    return newf


class checked(type):
    def __init__(self, name, parents, ns):
        for attr, obj in vars(self).items():
            if isinstance(obj, FunctionType) and not pref.match(attr):
                setattr(self, attr, checker(obj, attr))
        return super().__init__(name, parents, ns)

class E(metaclass=checked):
    def __init__(self, var: int):
        self.var = var if var % 2 else str(var)

    def mix(self, val: int, opt) -> int:
        return self.var * val + opt

    def al(self, c: int, d: int = 1, *e: int, f: int = 1, **g: int):
        return self.var * d


class E(metaclass=checked):
    def __init__(self, var: int):
        self.var = var if var%2 else str(var)

    def mix(self, val: int, opt) -> int:
        return self.var*val + opt

    def al(self, c: int, d:int=1, *e:int, f:int=1, **g:int):
        return self.var*d