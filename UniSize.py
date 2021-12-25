def sizer(cls):
    getattribute = cls.__getattribute__

    def new_getattr(obj, name):
        if name == "size":
            if hasattr(obj, "__len__"):
                return len(obj)
            elif hasattr(obj, "__abs__"):
                return abs(obj)
            return 0
        attr = getattribute(obj, name)
        return attr

    cls.__getattribute__ = new_getattr
    return cls

