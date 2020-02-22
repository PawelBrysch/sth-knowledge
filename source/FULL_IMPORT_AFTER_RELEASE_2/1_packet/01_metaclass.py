def call_clsinit(*args, **kwargs):
    cls = type(*args, **kwargs)
    cls._clsinit()
    return cls

class MyClass(metaclass=call_clsinit):
    @classmethod
    def _clsinit(cls):
        print("jestem w definicji!!!")






