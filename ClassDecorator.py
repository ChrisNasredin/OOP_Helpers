def decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
        def wrap(self):
            return 'wrapped metheod'
        def __getattr__(self, item):
            return getattr(self.wrapped, item)
    return Wrapper

class Human:
    def __init__(self, name, age):
        self.name = 'Andrey'
        self.age = age
    def __repr__(self):
        return f'Instance name is {self.name}, age {self.age}'

DecoHuman = decorator(Human)
'''
В имени DecoHuman содержится класс Wrapper, а присоединенным состоянием - класс Human.
При инициализации экземпляра класса Wrapped в атрибут self.wrapped сохраняется экземпляр, созданный из класса,
который находится в классе Human в объемлющей области
соотвветственно все атрибуты, которые не определены в классе будут делегированы обьекту в атрибуте self.wrapped 
После этого мы можем как угодно модицифицровать класс - атрибуты и методы декорируемого класса будут доступны через
self.wrapped.<атрибут>
'''
Andrey = DecoHuman('Andrey', 33)
print(Andrey.wrap())


print(Andrey.__class__.__bases__)