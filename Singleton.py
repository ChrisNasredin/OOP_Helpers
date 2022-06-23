def singleton(cls):
    '''
        декоратор паттерна singletone.
        При вызове класса для создания экземпляра проверяет, не создан ли
        уже экземпляр. Если экземпляр создан, возвращает уже созданный
        Реализация с помощью словаря. Не очень изящно
    '''
    instances = {}

    def inner(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return inner


def singleton_caps(cls):
    '''
        Более изящная инкапсулированная версия, мне она нравится больше
    '''
    Instance = None

    def inner(*args, **kwargs):
        nonlocal Instance
        if Instance is None:
            Instance = cls(*args, **kwargs)
        return Instance

    return inner


@singleton_caps
class Human:
    def __init__(self, name):
        self.name = name


A = Human('a')
B = Human('b')
C = Human('c')
D = Human('d')
print(A, B, C, D, sep='\n')
print(A is B is C is D)
