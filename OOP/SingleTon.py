class DB:                   # not perfect, __init__ of the second instance overwrites the first one
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name


a = DB('pg')
print(f'{a.name=}')
print(f'{id(a)=}')

b = DB('vertica')
print(f'{b.name=}')
print(f'{id(b)=}')


class MetaSingleton(type):              # __init__ is not overwritten
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    def __init__(self, name):
        self.name = name


logger1 = Logger('first')
logger2 = Logger('second')
print(logger1.name, logger2.name)
