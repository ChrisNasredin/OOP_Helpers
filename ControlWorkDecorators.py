# Написать пример декорирования класса функцией
import datetime
def DecoHuman(cls):
    class AdvHuman:
        class DescAge:
            def __init__(self, attr):
                self.attrib = attr

            def __get__(self, instance, owner):
                return int(datetime.datetime.now().year) - int(instance.birthday.split('.')[2])
        age = DescAge('age')
        def __init__(self, *args, **kwargs):
            self.InstHuman = cls(*args, **kwargs)
        #def __repr__(self):
        #    return f'Human\'s name is {self.InstHuman.name}, birhtday date - {self.InstHuman.birthday}'
        def __getattr__(self, item):
            return getattr(self.InstHuman, item)
    return AdvHuman

@DecoHuman
class Human:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

Andrey = Human('Andrey', '30.01.1989')
print(Andrey.age)

# Написать класс - декоратор

class DecoClass:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        return f'<p>{self.func(*args, **kwargs)}</p>'
@DecoClass
def mult(a,b):
    return a * b

print(mult(2,2))

# Написать декоратор с аргументами

def Decorator(*args):
    print(*args, 'arguments')
    def innerDecorator(func):
        def inner(*args, **kwargs):
            return f'<p>{func(*args, **kwargs)}</p>'
        return inner
    return innerDecorator

@Decorator(1,2,3)
def mult(a,b):
    return a * b
print(mult(2,2))