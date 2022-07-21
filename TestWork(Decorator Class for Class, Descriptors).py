# Написать декоратор Класса в виде класса, дескрипторы и эмуляция проперти через дескрипторы
import datetime


class Decorator:
    class Inner:
        class Descriptor:
            def __set_name__(self, owner, name):
                self.attr = name

            def __get__(self, instance, owner):
                if self.attr == 'age':
                    return int(datetime.datetime.now().year) - int(instance.birthday.split('.')[2])
                print('Descriptor Get')
                return getattr(object().instance, self.attr)

        class Property:
            def __init__(self, getr, setr=None, deleter=None, doc=None):
                self.getter = getr
                self.settr = setr
                self.deleter = deleter

            def setter(self, func):
                print('Set Setter')
                self.settr = func
                return self

            def __get__(self, instance, owner):
                return self.getter(instance)

            def __set__(self, instance, value):
                return self.settr(instance, value)

        age = Descriptor()
        name = Descriptor()

        def __init__(self, cls, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        @Property
        def sallary(self):
            print('Property Getter')
            inst = self.instance
            return object().inst.sallary

        @sallary.setter
        def sallary(self, value):
            print('Property Setter')
            inst = self.instance
            setattr(inst, 'sallary', value)

        def decorator_method(self):
            print(self.instance.name, 'say: I Love Decoration!')

        def __getattr__(self, item):
            return getattr(self.instance, item)

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        print('Object created')
        return Decorator.Inner(self.cls, *args, **kwargs)


@Decorator
class Human:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.sallary = 100

    def GetRaise(self, percent):
        if self.sallary != 0:
            self.sallary = self.sallary + (self.sallary / 100 * percent)
        else:
            print(self.name, 'hasn\'t job!')


Andrey = Human('Andrey', '30.01.1989')
Andrey.sallary = 10
Andrey.GetRaise(15)
print(Andrey.sallary)
Andrey.sallary = 500
print(Andrey.sallary)
Andrey.decorator_method()
print(Andrey.age)
print(Andrey.name)
